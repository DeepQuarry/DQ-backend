from typing import Generator
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core import config
from app.db.session import SessionLocal
from fastapi.security import OAuth2PasswordBearer

# tokenUrl is a relative url, so the if the API was @ https://example.com/
# then the token URL would be @ https://example.com/token
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login/acess-token")

valid_api_key = config.settings.API_KEY
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # use token authentication

def api_key_auth(api_key: str = Depends(oauth2_scheme)):
    if api_key not in valid_api_key:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")


def get_db() -> Generator:
    try:
        db: Session = SessionLocal()
        yield db
    finally:
        db.close()
