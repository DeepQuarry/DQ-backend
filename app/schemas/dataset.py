from typing import TYPE_CHECKING, List, Optional

from pydantic import BaseModel

from app.schemas.image import Image

if TYPE_CHECKING:
    from app.schemas.tag import TagBase


class DatasetBase(BaseModel):
    title: Optional[str] = None
    likes: Optional[int] = None
    dislikes: Optional[int] = None
    images: Optional[List[Image]] = None
    tags: Optional[List["TagBase"]] = None


class DatasetCreate(DatasetBase):
    title: str
    tags: List["TagBase"]


class DatasetUpdate(DatasetBase):
    title: str


class Dataset(DatasetBase):
    id: int

    class Config:
        orm_mode = True
