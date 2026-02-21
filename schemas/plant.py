from pydantic import BaseModel

class PlantCreate(BaseModel):
    name: str
    description: str | None = None

class PlantUpdate(PlantCreate):
    pass