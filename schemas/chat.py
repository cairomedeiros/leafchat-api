from pydantic import BaseModel

class ChatCreate(BaseModel):
    plant_id: str

class Chat(ChatCreate):
    id: str
    user_id: str
    summary: str | None
    created_at: str