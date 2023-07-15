from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base


class Image(Base):
    __tablename__ = "image"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    image_hash: Mapped[int]
    width: Mapped[int]
    height: Mapped[int]
    alt: Mapped[Optional[str]]
