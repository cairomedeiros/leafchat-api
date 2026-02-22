from fastapi import APIRouter, Depends
from ..auth.dependencies import get_current_user
from ..config.supabase import get_db
from ..schemas.watering_events import WateringEventCreate

router = APIRouter()

@router.post("/create")
async def create(watering_event: WateringEventCreate, 
                 current_user = Depends(get_current_user)):
        supabase = get_db()
        supabase.postgrest.auth(current_user["access_token"])

        response = (
            supabase.table("watering_events")
            .insert(watering_event.model_dump())
            .execute()
        )
        
        return response

@router.get("/list/{plant_id}")
async def list(plant_id: str, current_user=Depends(get_current_user)):
    supabase = get_db()
    supabase.postgrest.auth(current_user["access_token"])

    response = (
        supabase.table("watering_events")
        .select("*")
        .eq("plant_id", plant_id)
        .order("created_at", desc=True)
        .execute()
    )

    return response

@router.delete("/delete/{plant_id}")
async def delete(plant_id: str, current_user = Depends(get_current_user)):
        supabase = get_db()
        supabase.postgrest.auth(current_user["access_token"])

        response = (
            supabase.table("watering_events")
            .delete()
            .eq("plant_id", plant_id)
            .execute()
        )
        return response