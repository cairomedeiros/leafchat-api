from fastapi import APIRouter, Depends
from ..auth.dependencies import get_current_user
from ..config.supabase import get_db
from ..schemas import plant as PlantsSchemas

router = APIRouter()

@router.post("/create")
async def create(new_plant: PlantsSchemas.PlantBase, current_user = Depends(get_current_user)):
        supabase = get_db()

        supabase.postgrest.auth(current_user["access_token"])
        response = (
            supabase.table("plants")
            .insert(new_plant.model_dump())
            .execute()
        )
        
        return response

@router.patch("/upsert/{plant_id}")
async def upsert(plant_id: str, plant: PlantsSchemas.PlantBase, current_user = Depends(get_current_user)):
        supabase = get_db()

        supabase.postgrest.auth(current_user["access_token"])
        dado = plant.model_dump()
        response = (
            supabase.table("plants")
            .upsert({"id": plant_id, "name": dado["name"]})
            .execute()
        )
        return response

@router.get("/get/{plant_id}")
async def get(plant_id: str, current_user = Depends(get_current_user)):
        supabase = get_db()

        supabase.postgrest.auth(current_user["access_token"])
        response = (
            supabase.table("plants")
            .select("*")
            .eq("id", plant_id)
            .execute()
        )
        return response

@router.get("/list")
async def list(current_user = Depends(get_current_user)):
        supabase = get_db()

        supabase.postgrest.auth(current_user["access_token"])
        response = (
            supabase.table("plants")
            .select("*")
            .execute()
        )
        return response