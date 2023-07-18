from typing import Optional

from pydantic import BaseModel


class ImageBase(BaseModel):
    hash: Optional[str] = None
    path: Optional[str] = None
    dataset_id: Optional[int] = None


class ImageCreate(ImageBase):
    hash: str
    path: str
    dataset_id: int


class ImageUpdate(ImageBase):
    pass


class Image(ImageBase):
    id: int

    class Config:
        orm_mode = True
