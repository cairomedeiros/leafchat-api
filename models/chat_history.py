from sqlalchemy import (
    Column,
    ForeignKey,
    Enum as SQLAlchemyEnum,
    Text,
    DateTime,
    text
)
import enum
from sqlalchemy.dialects.postgresql import UUID
from .base import Base

class ChatRole(enum.Enum):
    USER = "user"
    ASSISTANT = "assistant"

class ChatHistory(Base):
    __tablename__ = "chat_history"
    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), index=True)
    plant_id = Column(UUID(as_uuid=True), ForeignKey("plants.id"), index=True)
    role = Column(
        SQLAlchemyEnum(ChatRole, name="chat_role_enum"),
        nullable=False,
        index=True
    )
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=text('now()'))