from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime

class Plant():
    __tablename__ = "plants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC), nullable=False)