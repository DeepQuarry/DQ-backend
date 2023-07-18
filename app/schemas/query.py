from typing import Optional

from pydantic import BaseModel


class QueryBase(BaseModel):
    query: Optional[str] = None
    subtask_completed: Optional[bool] = False


class QueryCreate(QueryBase):
    query: str
    subtask_completed: bool = False


class QueryUpdate(QueryBase):
    subtask_completed: bool = False


class Query(QueryBase):
    id: int

    class Config:
        orm_mode = True
