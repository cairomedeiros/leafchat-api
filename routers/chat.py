from fastapi import APIRouter, Depends, HTTPException
from ..auth.dependencies import get_current_user
from ..config.supabase import get_db
from ..schemas import chat as ChatSchemas

router = APIRouter()

@router.post("/create")
async def create(new_chat: ChatSchemas.ChatCreate, current_user = Depends(get_current_user)):
        supabase = get_db()
        supabase.postgrest.auth(current_user["access_token"])

        response = (
            supabase.table("chats")
            .insert(new_chat.model_dump())
            .execute()
        )

        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create chat.")
        
        return response.data[0]

@router.get("/get/{chat_id}", response_model=ChatSchemas.Chat)
async def get(chat_id: str, current_user = Depends(get_current_user)):
        supabase = get_db()
        supabase.postgrest.auth(current_user["access_token"])

        user_id = current_user["user"].id

        response = (
            supabase.table("chats")
            .select("*")
            .eq("id", chat_id)
            .eq("user_id", user_id)
            .single()
            .execute()
        )

        if not response.data:
            raise HTTPException(status_code=404, detail="Chat not found.")

        return response.data

@router.delete("/delete/{chat_id}", response_model=dict)
async def delete(chat_id: str, current_user = Depends(get_current_user)):
        supabase = get_db()
        supabase.postgrest.auth(current_user["access_token"])

        user_id = current_user["user"].id

        response = (
            supabase.table("chats")
            .delete()
            .eq("id", chat_id)
            .eq("user_id", user_id)
            .execute()
        )

        return response.data[0]