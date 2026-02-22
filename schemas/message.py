from pydantic import BaseModel

class MessageCreate(BaseModel):
    chat_id: str
    role: str
    content: str
    image_path: str | None = None

async def chat_form(
    chat_id: str,
    content: str,
    image_path: str | None = None
) -> MessageCreate:
    return MessageCreate(
        chat_id=chat_id,
        content=content,
        image_path=image_path
    )