from io import BytesIO
import os
import random
import time
from typing import Dict, List
import urllib.parse
import requests
from requests_ip_rotator import ApiGateway
import socket
from threading import Thread, BoundedSemaphore, Lock
import re
import imghdr
import hashlib
import posixpath
import shutil

from app.core.log import generate_logger

logger = generate_logger("Scraper")

class Scraper:
    DOMAIN = "https://www.bing.com"

    DEFAULT_REGIONS = ["us-east-1", "us-east-2"]
    DEFAULT_USER_AGENTS = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    ]
    DEFAULT_HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Dnt": "1",
        "Upgrade-Insecure-Requests": "1",
    }

    def __init__(
        self,
        is_testing: bool = True,
        threads: int = 10,
        image_limit: int = 50,
        is_adult: bool = False,
        REGIONS: List[str] = DEFAULT_REGIONS,
        USER_AGENTS: List[str] = DEFAULT_USER_AGENTS,
        HEADERS: Dict[str, str] = DEFAULT_HEADERS,
        AWS_ACCESS_KEY_ID: str | None = None,
        AWS_ACCESS_KEY_SECRET: str | None = None,
    ):
        self.is_testing = is_testing
        self.headers = HEADERS
        self.regions = REGIONS
        self.aws_key = AWS_ACCESS_KEY_ID
        self.aws_secret = AWS_ACCESS_KEY_SECRET
        self.image_limit = image_limit
        self.image_hashes = {}
        self.downloaded_urls = set()
        self.download_semaphore = BoundedSemaphore(threads)
        self.file_lock = Lock()
        self.session = None

        user_agent = random.choice(USER_AGENTS)
        self.headers["User-Agent"] = user_agent

        if is_adult:
            self.headers["Cookie"] = "SRCHHPGUSR=ADLT=OFF"

        socket.setdefaulttimeout(2)

    def __encode_url(self, url):
        scheme, netloc, path, query, fragment = list(urllib.parse.urlsplit(url))

        path = urllib.parse.quote(path)
        query = urllib.parse.quote_plus(query)
        fragment = urllib.parse.quote(fragment)

        encoded_url = urllib.parse.urlunsplit((scheme, netloc, path, query, fragment))

        return encoded_url


    def get_upload_dir(self, query_id: int) -> str:
        if self.is_testing:
            return os.path.join("app", ".cache", "datasets", str(query_id))
        else:
            raise NotImplementedError("Server side upload not implemented yet")

    def download_image(self, url: str, upload_dir: str):
        if url in self.downloaded_urls:
            logger.warning(f"SKIP: Already downloaded url: {url}")
            return
        
        self.download_semaphore.acquire()

        path = urllib.parse.urlsplit(url).path
        name, _ = os.path.splitext(posixpath.basename(path))
        if not name:
            # if path and name are empty (e.g. https://sample.domain/abcd/?query)
            name = hashlib.md5(url.encode('utf-8')).hexdigest()
        name = name.strip()[:36].strip()

        try:
            url.encode("ascii")
        except UnicodeEncodeError:
            url = self.__encode_url(url)

        try:
            response = self.session.get(url, headers=self.headers)
            image = response.content
            imgtype = imghdr.what(BytesIO(image), image)
            if not imgtype:
                logger.warning(f"SKIP: Invalid image, not downloading: {name}")
                return

            ext = "jpg" if imgtype == "jpeg" else imgtype
            filename = name + "." + ext

            hash = hashlib.md5(image).hexdigest()
            if hash in self.image_hashes:
                logger.warning(f"SKIP: Already downloaded {filename}, not saving")
                return

            counter = 0
            target_filepath = os.path.join(upload_dir, filename)
            while os.path.exists(target_filepath):
                if hashlib.md5(open(target_filepath, 'rb').read()).hexdigest() == hash:
                    logger.warning(f"SKIP: Already downloaded {filename}, not saving")
                    return

                counter += 1
                filename = "%s-%d.%s" % (name, counter, ext)
                target_filepath = os.path.join(upload_dir, filename)

            self.image_hashes[hash] = filename

            self.file_lock.acquire()
            if len(self.downloaded_urls) > self.image_limit:
                return

            with open(target_filepath, "wb") as f:
                f.write(image)

            logger.info(f"DOWNLOADED: {filename}")
            self.downloaded_urls.add(url)

        except Exception as e:
            logger.error("FAIL: " + name, str(e))

        finally:
            self.download_semaphore.release()

            if self.file_lock.locked():
                self.file_lock.release()



    def scrape_images(self, query: str, query_id: int):
        upload_dir = self.get_upload_dir(query_id)
        if self.is_testing:
            shutil.rmtree(upload_dir)

        os.mkdir(upload_dir)

        images_downloaded = 1
        cleaned_query = urllib.parse.quote_plus(query)
        last = ""

        with ApiGateway(
            self.DOMAIN,
            regions=self.regions,
            access_key_id=self.aws_key,
            access_key_secret=self.aws_secret
        ) as g:

            self.session = requests.Session()
            self.session.mount(self.DOMAIN, g)

            while True:
                time.sleep(0.1)

                url = "https://www.bing.com/images/async?q=" + cleaned_query + "&first=" + str(images_downloaded) + "&count=35&qft="
                response = self.session.get(url, headers=self.headers)
                links = re.findall('murl&quot;:&quot;(.*?)&quot;', response.text)

                try:
                    if links[-1] == last:
                        return

                    for link in links:
                        if len(self.downloaded_urls) > self.image_limit:
                            return

                        thread = Thread(target=self.download_image, args=(link, upload_dir))
                        thread.start()

                    last = links[-1]
                    images_downloaded += 1

                except Exception as e:
                    logger.error(f"FAIL: Failed to download '{query}': {str(e)}")



def test_scraper():
    scraper = Scraper(image_limit=10)
    scraper.scrape_images("munchkin", 1)

if __name__ == "__main__":
    test_scraper()