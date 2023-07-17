import random
from typing import Dict, List

import requests
from bs4 import BeautifulSoup
from requests import Response
from requests_ip_rotator import ApiGateway


class Scraper:
    SITE = "https://www.google.com"
    SEARCH = SITE + "/search"
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
    DEFAULT_PARAMS = {"gl": "us", "hl": "en", "tbm": "isch"}

    def __init__(
        self,
        query: str,
        query_id: int,
        is_testing: bool = False,
        REGIONS: List[str] = DEFAULT_REGIONS,
        USER_AGENTS: List[str] = DEFAULT_USER_AGENTS,
        HEADERS: Dict[str, str] = DEFAULT_HEADERS,
        PARAMS: Dict[str, str] = DEFAULT_PARAMS,
        AWS_ACCESS_KEY_ID: str | None = None,
        AWS_ACCESS_KEY_SECRET: str | None = None,
    ):
        self.query_id = query_id
        self.is_testing = is_testing
        self.headers = HEADERS
        self.params = PARAMS
        self.params["q"] = query

        user_agent = random.choice(USER_AGENTS)
        self.headers["User-Agent"] = user_agent

        self.gateway = ApiGateway(
            self.SITE,
            regions=REGIONS,
            access_key_id=AWS_ACCESS_KEY_ID,
            access_key_secret=AWS_ACCESS_KEY_SECRET,
        )

    def start_gateway(self):
        self.gateway.start()

    def shutdown_gateway(self):
        self.gateway.shutdown()

    def upload_images(self, img_responses: List[Response]):
        if self.is_testing:
            # todo
            pass

        else:
            raise NotImplementedError("Have not implemented non-testing image upload")

    def write_to_cache(self):
        with open("app/.cache/test.html", "r") as f:
            content = f.read()
            soup = BeautifulSoup(content, "html.parser")
            imgs = soup.find_all("img", attrs={"class": "yWs4tf"})
            print(len(imgs))

            with open("app/.cache/test.jpg", "wb") as i:
                r = requests.get(imgs[0]["src"])
                i.write(r.content)

    def scrape(self) -> BeautifulSoup:
        session = requests.Session()
        session.mount(self.SITE, self.gateway)

        response = session.get(self.SEARCH, params=self.params)
        print("Gateway Response:", response.status_code)
        soup = BeautifulSoup(response.content, "html.parser")

        with open("app/.cache/test.html", "w") as f:
            f.write(soup.prettify())

        return soup


if __name__ == "__main__":
    pass
