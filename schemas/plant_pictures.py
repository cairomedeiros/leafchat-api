from pydantic import BaseModel

class PlantPicture(BaseModel):
    id: str
    plant_id: str
    image_path: str | None
    created_at: str