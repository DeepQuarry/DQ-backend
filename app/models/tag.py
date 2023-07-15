from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base


class Tag(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    datasets: Mapped[List["Dataset"]] = relationship(  # type: ignore
        secondary="dataset_tag", back_populates="tags"
    )
