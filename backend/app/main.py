from fastapi import FastAPI
from app.api.endpoints import router as api_router

app = FastAPI(title="Tonalogy API")

app.include_router(api_router)

