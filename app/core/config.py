from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_USER: str
    APP_IP: str
    APP_DB: str


settings = Settings()

TESTING = True
