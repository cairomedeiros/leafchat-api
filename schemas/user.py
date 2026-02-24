from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    disabled: bool | None = None

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserSession(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int
    token_type: str