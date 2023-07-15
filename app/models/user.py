from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base
from app.models.image import Image
from app.models.tag import Tag

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str]
    username: Mapped[str]
    hashed_password: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(default=False)
    liked_datasets: Mapped[List["Dataset"]] = relationship(secondary="liked_dataset") # type: ignore
    created_datasets: Mapped[List["Dataset"]] = relationship(secondary="created_dataset") # type: ignore
