from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base


class Query(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    query: Mapped[str]
    subtask_completed: Mapped[bool] = mapped_column(default=False)

    dataset: Mapped["Dataset"] = relationship(back_populates="query")
