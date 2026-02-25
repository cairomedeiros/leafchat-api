from pydantic import BaseModel

class MessageCreate(BaseModel):
    chat_id: str
    content: str | None

class Message(MessageCreate):
    id: int
    role: str
    image_path: str | None
    created_at: str

async def chat_form(
    chat_id: str,
    content: str | None,
) -> MessageCreate:
    return MessageCreate(
        chat_id=chat_id,
        content=content,
    )