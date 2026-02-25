from fastapi import APIRouter, Depends, HTTPException
from ..auth.dependencies import get_current_user
from ..config.supabase import get_db
from ..schemas import watering_events as WateringSchemas

router = APIRouter()

@router.post("/create", response_model=WateringSchemas.WateringEvent)
async def create(watering_event: WateringSchemas.WateringEventCreate, 
                 current_user = Depends(get_current_user)):
        supabase = get_db()
        supabase.postgrest.auth(current_user["access_token"])

        response = (
            supabase.table("watering_events")
            .insert(watering_event.model_dump())
            .execute()
        )

        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create watering event.")
        
        return response.data[0]

@router.get("/list/{plant_id}", response_class=list[WateringSchemas.WateringEvent])
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

    if not response.data:
        raise HTTPException(status_code=404, detail="No watering events found for this plant.")

    return response.data

@router.delete("/delete/{plant_id}", response_model=dict)
async def delete(plant_id: str, current_user = Depends(get_current_user)):
        supabase = get_db()
        supabase.postgrest.auth(current_user["access_token"])

        response = (
            supabase.table("watering_events")
            .delete()
            .eq("plant_id", plant_id)
            .execute()
        )

        if not response.data:
            raise HTTPException(status_code=404, detail="No watering events found for this plant.")

        return response.data[0]