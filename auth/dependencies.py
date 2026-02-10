
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from ..config import supabase

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        supabase_db = supabase.get_db()
        user = supabase_db.auth.get_user(token)
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")