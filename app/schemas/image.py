from typing import Optional

from pydantic import BaseModel


class ImageBase(BaseModel):
    image_hash: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    alt: Optional[str] = None


class ImageCreate(ImageBase):
    width: int
    height: int


class ImageUpdate(ImageBase):
    alt: str


class Image(ImageBase):
    id: int

    class Config:
        orm_mode = True
