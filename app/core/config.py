from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    API_KEY: str

    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_BUCKET: str = "deepquarrybucket"

    # Heroku designates the primary DB with this config var
    DATABASE_URL: Optional[str] = None

    POSTGRES_USER: Optional[str]
    POSTGRES_PASSWORD: Optional[str] = None
    POSTGRES_IP: Optional[str]
    POSTGRES_PORT: Optional[str] = None
    POSTGRES_DB: Optional[str]

    PROJECT_NAME = "DeepQuarry API v1"
    TESTING: int = 1


settings = Settings()
