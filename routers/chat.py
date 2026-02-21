from fastapi import APIRouter, Depends
from ..auth.dependencies import get_current_user
from ..config.supabase import get_db
from ..schemas import chat as ChatSchemas

router = APIRouter()

@router.post("/create")
async def create(new_chat_message: ChatSchemas.ChatCreate, current_user = Depends(get_current_user)):
        supabase = get_db()
        supabase.postgrest.auth(current_user["access_token"])

        response = (
            supabase.table("chat")
            .insert(new_chat_message.model_dump())
            .execute()
        )
        
        return response

@router.get("/get/{chat_id}")
async def get(chat_id: str, current_user = Depends(get_current_user)):
        supabase = get_db()
        supabase.postgrest.auth(current_user["access_token"])

        user_id = current_user["user"].id

        response = (
            supabase.table("chat")
            .select("*")
            .eq("id", chat_id)
            .eq("user_id", user_id)
            .single()
            .execute()
        )
        return response

@router.delete("/delete/{chat_id}")
async def delete(chat_id: str, current_user = Depends(get_current_user)):
        supabase = get_db()
        supabase.postgrest.auth(current_user["access_token"])

        user_id = current_user["user"].id

        response = (
            supabase.table("chat")
            .delete()
            .eq("id", chat_id)
            .eq("user_id", user_id)
            .execute()
        )
        return response