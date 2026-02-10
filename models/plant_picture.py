from sqlalchemy import Column, Integer, Text, String, ForeignKey, DateTime
from datetime import datetime

class PlantPicture():
    __tablename__ = "plant_pictures"
    id = Column(Integer, primary_key=True, index=True)
    file_url = Column(String(350), nullable=False)
    plant_id = Column(Integer, ForeignKey("plants.id"), index=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC), nullable=False)