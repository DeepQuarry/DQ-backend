from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base


class Query(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    query: Mapped[str]
    subtask_completed: Mapped[bool] = mapped_column(default=False)
    threads: Mapped[int] = mapped_column(default=20)
    image_limit: Mapped[int] = mapped_column(default=100)
    is_adult: Mapped[bool] = mapped_column(default=False)
