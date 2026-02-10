from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    disabled: bool | None = None

class UserCreate(UserBase):
    password: str

class UserOut(BaseModel):
    id: str