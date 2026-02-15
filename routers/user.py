from fastapi import APIRouter
from ..schemas import user as UserSchemas
from ..config.supabase import get_db

router = APIRouter()

@router.post("/sign_up")
async def sign_up(new_user: UserSchemas.UserCreate):
        supabase = get_db()

        response = supabase.auth.sign_up(
                {
                        "email": new_user.email,
                        "password": new_user.password,
                }
        )
        
        return response

@router.post("/login")
async def login(user: UserSchemas.UserLogin):
        supabase = get_db()

        response = supabase.auth.sign_in_with_password(
                {
                        "email": user.email,
                        "password": user.password,
                }
        )
        return response.session