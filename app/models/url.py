
from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.user import UserORM

class UrlORM(Base):
    __tablename__ = "urls"

    id: Mapped[int] = mapped_column(primary_key=True)
    original_url: Mapped[str]
    short_url: Mapped[str]
    user_id: Mapped[str] = relationship(UserORM.id)
    created_at: Mapped[str] = mapped_column(Date())