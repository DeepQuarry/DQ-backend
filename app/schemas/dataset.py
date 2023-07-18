from typing import List, Optional

from pydantic import BaseModel

from app.schemas.image import Image


class DatasetBase(BaseModel):
    title: Optional[str] = None
    query_id: Optional[int] = None
    images: Optional[List[Image]] = None


class DatasetCreate(DatasetBase):
    query_id: int
    title: str
    images: List[Image] = []


class DatasetUpdate(DatasetBase):
    title: str


class Dataset(DatasetBase):
    id: int

    class Config:
        orm_mode = True
