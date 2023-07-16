from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base
from app.models.image import Image
from app.models.query import Query


class Dataset_Image(Base):
    dataset_id: Mapped[int] = mapped_column(ForeignKey("dataset.id"), primary_key=True)
    image_id: Mapped[int] = mapped_column(ForeignKey("image.id"), primary_key=True)


class Liked_Dataset(Base):
    dataset_id: Mapped[int] = mapped_column(ForeignKey("dataset.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)


class Created_Dataset(Base):
    dataset_id: Mapped[int] = mapped_column(ForeignKey("dataset.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)


class Dataset(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    likes: Mapped[int]
    dislikes: Mapped[int]

    query: Mapped["Query"] = relationship(back_populates="dataset")
    images: Mapped[List["Image"]] = relationship(
        secondary="dataset_image", back_populates="datasets"
    )
