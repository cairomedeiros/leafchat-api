from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, text
from sqlalchemy.dialects.postgresql import UUID
from .base import Base

class Plant(Base):
    __tablename__ = "plants"
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(255), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), index=True)
    created_at = Column(DateTime, server_default=text('now()'), nullable=False)