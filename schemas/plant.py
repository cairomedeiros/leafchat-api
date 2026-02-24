from pydantic import BaseModel

class PlantCreate(BaseModel):
    name: str
    description: str | None = None

class PlantUpdate(PlantCreate):
    pass

class Plant(PlantCreate):
    id: str
    user_id: str
    created_at: str
    file_path: str | None = None