from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    API_KEY: str

    AWS_ACCESS_KEY_ID: str
    AWS_ACCESS_KEY_SECRET: str

    POSTGRES_USER: str
    POSTGRES_PASSWORD: Optional[str] = None
    POSTGRES_IP: str
    POSTGRES_PORT: Optional[str] = None
    POSTGRES_DB: str

    PROJECT_NAME = "DeepQuarry API v1"
    TESTING: bool = True


settings = Settings()
