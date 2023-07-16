from typing import Generator
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db.session import SessionLocal


# tokenUrl is a relative url, so the if the API was @ https://example.com/
# then the token URL would be @ https://example.com/token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login/acess-token")

def get_db() -> Generator:
    try:
        db: Session = SessionLocal()
        yield db
    finally:
        db.close()
