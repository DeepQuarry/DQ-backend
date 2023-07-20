import os
import shutil
import boto3
from rq import Queue
from app.core.log import generate_logger
from app.worker import conn
from app.core.config import settings


logger = generate_logger()
worker_queue = Queue(connection=conn)

class Uploader:
    def __init__(self) -> None:
        self.s3 = boto3.resource("s3")

        for bucket in self.s3.buckets.all():
            logger.info(f"Registered bucket {bucket}")

        self.bucket_name = settings.AWS_BUCKET

    def load_query(self, query_id: int):
        self.query_id = query_id

    def get_dir(self) -> str:
        if settings.TESTING:
            return os.path.join("app", ".cache", str(self.query_id))
        else:
            return str(self.query_id)

    def get_fpath(self, fname: str) -> str:
        return os.path.join(self.get_dir(), fname)

    def create_dir(self) -> str:
        upload_dir = self.get_dir()
        if settings.TESTING:
            if os.path.exists(upload_dir):
                shutil.rmtree(upload_dir)
            os.mkdir(upload_dir)
        else:
            self.s3.Bucket(self.bucket_name).put_object(Key=upload_dir+"/")


    def queue_upload(self, fname: str, image: bytes):
        def upload(self, fname: str, image: bytes):
            path = self.get_fpath(fname)
            self.s3.Bucket(self.bucket_name).put_object(Key=path, Body=image)

        worker_queue.enqueue(upload, fname, image)

