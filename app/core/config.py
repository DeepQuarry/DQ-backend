from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    APP_USER: str
    APP_IP: str
    APP_DB: str

    PROJECT_NAME = "DeepQuarry API v1"
    TESTING: bool = True


settings = Settings()
