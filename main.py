from fastapi import FastAPI
from src.routers.lamoda import router

app = FastAPI()

app.include_router(router)
