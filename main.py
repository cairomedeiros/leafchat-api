from fastapi import FastAPI
from .routers import user, plant

app = FastAPI()
app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(plant.router, prefix="/plant", tags=["plant"])

@app.get("/")
async def root():
			return {"message": "Hello World"}