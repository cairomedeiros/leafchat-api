from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from ..auth.dependencies import get_current_user
from ..config.supabase import get_db
from ..schemas import plant_pictures as PlantPictureSchemas
import os, uuid

router = APIRouter()

@router.post("/create", response_model=PlantPictureSchemas.PlantPicture)
async def create(image: UploadFile | None = File(default=None), 
                 plant_id: str = None, 
                 current_user = Depends(get_current_user)):
        supabase = get_db()
        supabase.postgrest.auth(current_user["access_token"])
        plant_picture = {
            "plant_id": plant_id,
        }

        contents = await image.read()

        image_ext = os.path.splitext(image.filename)[1]
        image_name = f"{uuid.uuid4()}{image_ext}"
        image_path = f"{current_user['user'].id}/{image_name}"

        plant_picture["image_path"] = image_path
        
        response = supabase.storage.from_('leafchat').upload(image_path, contents)

        response = (
            supabase.table("plant_pictures")
            .insert(plant_picture)
            .execute()
        )

        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create plant picture.")
        
        return response.data[0]

@router.get("/list/{plant_id}", response_class=list[PlantPictureSchemas.PlantPicture])
async def list(plant_id: str, current_user=Depends(get_current_user)):
    supabase = get_db()
    supabase.postgrest.auth(current_user["access_token"])

    response = (
        supabase.table("plant_pictures")
        .select("*")
        .eq("plant_id", plant_id)
        .order("created_at", desc=True)
        .execute()
    )

    if not response.data:
        raise HTTPException(status_code=404, detail="No pictures found for this plant.")

    return response.data

@router.delete("/delete/{plant_id}", response_model=dict)
async def delete(plant_id: str, current_user = Depends(get_current_user)):
        supabase = get_db()
        supabase.postgrest.auth(current_user["access_token"])

        response = (
            supabase.table("plant_pictures")
            .delete()
            .eq("plant_id", plant_id)
            .execute()
        )
        return response.data[0]