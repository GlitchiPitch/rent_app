import uuid

from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base

class Ad(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[uuid.UUID] = mapped_column(nullable=False)
    room_count: Mapped[int]
    cost: Mapped[int]
    address: Mapped[str | None] = None