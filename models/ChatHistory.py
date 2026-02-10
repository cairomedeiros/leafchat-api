from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Enum as SQLAlchemyEnum,
    Text,
    DateTime
)
import enum
from datetime import datetime

class ChatRole(enum.Enum):
    USER = "user"
    ASSISTANT = "assistant"

class ChatHistory():
    __tablename__ = "chat_history"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), index=True)
    role = Column(
        SQLAlchemyEnum(ChatRole, name="chat_role_enum"),
        nullable=False,
        index=True
    )
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC), nullable=False)