from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base
from app.models.image import Image
from app.models.tag import Tag


class DatasetTag(Base):
    __tablename__ = "dataset_tag"

    dataset_id: Mapped[int] = mapped_column(ForeignKey("dataset.id"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"), primary_key=True)


class DatasetImage(Base):
    __tablename__ = "dataset_image"

    dataset_id: Mapped[int] = mapped_column(ForeignKey("dataset.id"), primary_key=True)
    image_id: Mapped[int] = mapped_column(ForeignKey("image.id"), primary_key=True)


class LikedDataset(Base):
    __tablename__ = "liked_dataset"

    dataset_id: Mapped[int] = mapped_column(ForeignKey("dataset.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)


class CreatedDataset(Base):
    __tablename__ = "created_dataset"

    dataset_id: Mapped[int] = mapped_column(ForeignKey("dataset.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)


class Dataset(Base):
    __tablename__ = "dataset"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    likes: Mapped[int]
    dislikes: Mapped[int]
    images: Mapped[List["Image"]] = relationship(
        secondary="dataset_image", back_populates="datasets"
    )
    tags: Mapped[List["Tag"]] = relationship(
        secondary="dataset_tag", back_populates="datasets"
    )
