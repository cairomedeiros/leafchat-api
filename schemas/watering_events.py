from pydantic import BaseModel

class WateringEventCreate(BaseModel):
    plant_id: str
    watered_at: str