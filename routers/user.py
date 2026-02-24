from fastapi import APIRouter, HTTPException, HTTPException
from ..schemas import user as UserSchemas
from ..config.supabase import get_db

router = APIRouter()

@router.post("/sign_up", response_model=UserSchemas.UserSession)
async def sign_up(new_user: UserSchemas.UserCreate):
        supabase = get_db()

        response = supabase.auth.sign_up(
                {
                        "email": new_user.email,
                        "password": new_user.password,
                }
        )

        if not response.user:
                raise HTTPException(status_code=400, detail="Signup failed")

        session = response.session
        
        return {
                "access_token": session.access_token, 
                "refresh_token": session.refresh_token, 
                "expires_in": session.expires_in, 
                "token_type": session.token_type,
        }

@router.post("/login", response_model=UserSchemas.UserSession)
async def login(user: UserSchemas.UserLogin):
        supabase = get_db()

        response = supabase.auth.sign_in_with_password(
                {
                        "email": user.email,
                        "password": user.password,
                }
        )
        if not response.user:
                raise HTTPException(status_code=400, detail="Login failed")

        session = response.session
        return {
                "access_token": session.access_token, 
                "refresh_token": session.refresh_token, 
                "expires_in": session.expires_in, 
                "token_type": session.token_type,
        }