from pydantic import BaseModel


class Image(BaseModel):
    hash: str
    path: str
    id: int

    class Config:
        orm_mode = True
