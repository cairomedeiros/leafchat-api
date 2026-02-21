from pydantic import BaseModel

class ChatCreate(BaseModel):
    plant_id: str