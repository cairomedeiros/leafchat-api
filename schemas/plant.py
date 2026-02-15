from pydantic import BaseModel

class PlantBase(BaseModel):
    name: str