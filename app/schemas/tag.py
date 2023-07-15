from typing import TYPE_CHECKING, List, Optional

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemas.dataset import DatasetBase


class TagBase(BaseModel):
    title: Optional[str]
    datasets: Optional[List["DatasetBase"]] = None


class TagCreate(TagBase):
    title: str
    datasets: List["DatasetBase"]


class TagUpdate(TagBase):
    title: str
    datasets: List["DatasetBase"]


class Tag(TagBase):
    id: int

    class Config:
        orm_mode = True
