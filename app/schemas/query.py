from typing import Optional

from pydantic import BaseModel


class QueryBase(BaseModel):
    query: Optional[str] = None
    subtask_completed: Optional[bool] = False
    threads: Optional[int] = None
    image_limit: Optional[int] = None
    is_adult: Optional[bool] = None


class QueryCreate(QueryBase):
    query: str
    subtask_completed: bool = False
    threads: int = 20
    image_limit: int = 100
    is_adult: bool = False


class QueryUpdate(QueryBase):
    subtask_completed: bool = False


class Query(QueryBase):
    id: int

    class Config:
        orm_mode = True
