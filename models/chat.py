from sqlalchemy import (
    Column,
    ForeignKey,
    String,
    Text,
    DateTime,
    text
)
from sqlalchemy.dialects.postgresql import UUID
from .base import Base

class Chat(Base):
    __tablename__ = "chats"
    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String(255), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), index=True)
    plant_id = Column(UUID(as_uuid=True), ForeignKey("plants.id"), nullable=True)
    summary = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=text('now()'))