from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str]
    username: Mapped[str]
    hashed_password: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(default=False)
    min_last_active: Mapped[int] = mapped_column(default=0)
    # liked_datasets: Mapped[List["Dataset"]] = relationship(secondary="liked_dataset")  # type: ignore
    # created_datasets: Mapped[List["Dataset"]] = relationship(secondary="created_dataset")  # type: ignore
