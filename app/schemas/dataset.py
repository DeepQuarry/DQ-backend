from typing import TYPE_CHECKING, List, Optional

from pydantic import BaseModel

from app.schemas.image import Image

class DatasetBase(BaseModel):
    title: Optional[str] = None
    query_id: Optional[int] = None
    likes: Optional[int] = None
    dislikes: Optional[int] = None
    images: Optional[List[Image]] = None


class DatasetCreate(DatasetBase):
    title: str


class DatasetUpdate(DatasetBase):
    title: str


class Dataset(DatasetBase):
    id: int

    class Config:
        orm_mode = True
