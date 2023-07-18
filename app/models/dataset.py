from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base
from app.models.image import Image

# needed for Alembic to recognize query_id ForeignKey
from app.models.query import Query  # pyright: ignore


class Dataset(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]

    query_id: Mapped[int] = mapped_column(ForeignKey("query.id"))
    images: Mapped[List["Image"]] = relationship()
