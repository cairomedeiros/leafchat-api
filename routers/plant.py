from fastapi import APIRouter, Depends, HTTPException
from ..auth.dependencies import get_current_user
from ..config.supabase import get_db
from ..schemas import plant as PlantsSchemas

router = APIRouter()

@router.post("/create", response_model=PlantsSchemas.Plant)
async def create(new_plant: PlantsSchemas.PlantCreate, 
                 current_user = Depends(get_current_user)):
        supabase = get_db()
        supabase.postgrest.auth(current_user["access_token"])
        response = (
            supabase.table("plants")
            .insert(new_plant.model_dump())
            .execute()
        )
        if response.data is None:
                raise HTTPException(status_code=400, detail="Failed to create plant")
        
        return response.data[0]

@router.patch("/upsert/{plant_id}", response_model=PlantsSchemas.Plant)
async def upsert(plant_id: str,
                 plant: PlantsSchemas.PlantUpdate,
                 current_user = Depends(get_current_user)):
        supabase = get_db()
        supabase.postgrest.auth(current_user["access_token"])

        update_data = {
                "name": plant.name,
                "description": plant.description
        }
        response = (
            supabase.table("plants")
            .upsert({**update_data, "id": plant_id})
            .execute()
        )
        if response.data is None:
                raise HTTPException(status_code=400, detail="Failed to update plant")

        return response.data[0]

@router.get("/get/{plant_id}", response_model=PlantsSchemas.Plant)
async def get(plant_id: str, current_user=Depends(get_current_user)):
    supabase = get_db()
    supabase.postgrest.auth(current_user["access_token"])

    user_id = current_user["user"].id

    response = (
        supabase.table("plants")
        .select("*")
        .eq("id", plant_id)
        .eq("user_id", user_id)
        .single()
        .execute()
    )

    if not response.data:
        raise HTTPException(status_code=404, detail="Plant not found")

    return response.data

@router.get("/list", response_model=list[PlantsSchemas.Plant])
async def list(current_user=Depends(get_current_user)):
    supabase = get_db()
    supabase.postgrest.auth(current_user["access_token"])

    user_id = current_user["user"].id

    response = (
        supabase.table("plants")
        .select("*")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .execute()
    )
    if response.data is None:
        raise HTTPException(status_code=400, detail="Failed to list plants")

    return response.data