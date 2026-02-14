from sqlalchemy import Column, Text, String, ForeignKey, DateTime, text
from sqlalchemy.dialects.postgresql import UUID
from .base import Base

class PlantPicture(Base):
    __tablename__ = "plant_pictures"
    id = Column(UUID(as_uuid=True), primary_key=True)
    file_url = Column(String(400), nullable=False)
    plant_id = Column(UUID(as_uuid=True), ForeignKey("plants.id"), index=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=text('now()'))