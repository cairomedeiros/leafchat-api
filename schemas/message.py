from pydantic import BaseModel

class MessageCreate(BaseModel):
    chat_id: str
    role: str
    content: str

async def chat_form(
    chat_id: str,
    content: str,
) -> MessageCreate:
    return MessageCreate(
        chat_id=chat_id,
        content=content,
    )