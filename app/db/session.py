from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

def create_postgres_url():
    if settings.DATABASE_URL:
        return settings.DATABASE_URL
    else:
        return f"postgresql://{settings.POSTGRES_USER}{':' + settings.POSTGRES_PASSWORD if settings.POSTGRES_PASSWORD else ''}@{settings.POSTGRES_IP}{':' + settings.POSTGRES_PORT if settings.POSTGRES_PORT else ''}/{settings.POSTGRES_DB}"

SQLALCHEMY_DATABASE_URL = create_postgres_url()

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
