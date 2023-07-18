from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base


class Image(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    hash: Mapped[str]
    path: Mapped[str]

    dataset_id: Mapped[int] = mapped_column(ForeignKey("dataset.id"))
