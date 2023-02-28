from fastapi import FastAPI
from src.routers.lamoda import router
from src.routers.twitch import router_twitch

app = FastAPI()

app.include_router(router)
app.include_router(router_twitch)

