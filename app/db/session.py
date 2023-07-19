from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{settings.POSTGRES_USER}{':' + settings.POSTGRES_PASSWORD if settings.POSTGRES_PASSWORD else ''}@{settings.POSTGRES_IP}{':' + settings.POSTGRES_PORT if settings.POSTGRES_PORT else ''}/{settings.POSTGRES_DB}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
