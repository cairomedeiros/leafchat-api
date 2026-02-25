from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from ..auth.dependencies import get_current_user
from ..config.supabase import get_db
from ..schemas import message as MessageSchemas
import os, uuid
from ..enums.chat_role import ChatRole

router = APIRouter()

@router.post("/create", response_model=MessageSchemas.Message)
async def create(image: UploadFile | None = File(default=None), 
                 new_message: MessageSchemas.MessageCreate = Depends(MessageSchemas.chat_form), 
                 current_user = Depends(get_current_user)):
        supabase = get_db()
        supabase.postgrest.auth(current_user["access_token"])

        if not new_message.content and not image:
            raise HTTPException(status_code=400, detail="A message must have either content or an image.")

        image_path = None

        if image:
            contents = await image.read()

            image_ext = os.path.splitext(image.filename)[1]
            image_name = f"{uuid.uuid4()}{image_ext}"
            image_path = f"{current_user['user'].id}/{image_name}"
            
            response = supabase.storage.from_('leafchat').upload(image_path, contents)

        message_data = {
            "chat_id": new_message.chat_id,
            "role": ChatRole.USER.value,
            "content": new_message.content,
            "image_path": image_path
        }

        response = (
            supabase.table("messages")
            .insert(message_data)
            .execute()
        )

        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create message.")
        
        return response.data[0]      

@router.get("/list/{chat_id}", response_class=list[MessageSchemas.Message])
async def list(chat_id: str, current_user=Depends(get_current_user)):
    supabase = get_db()
    supabase.postgrest.auth(current_user["access_token"])

    response = (
        supabase.table("messages")
        .select("*")
        .eq("chat_id", chat_id)
        .order("created_at", desc=True)
        .execute()
    )

    if not response.data:
        raise HTTPException(status_code=404, detail="No messages found for this chat.")
    
    return response.data

@router.delete("/delete/{chat_id}/{message_id}", response_model=dict)
async def delete(chat_id: str, message_id: int, current_user = Depends(get_current_user)):
        supabase = get_db()
        supabase.postgrest.auth(current_user["access_token"])

        response = (
            supabase.table("messages")
            .delete()
            .eq("chat_id", chat_id)
            .eq("id", message_id)
            .execute()
        )
        return response.data[0]