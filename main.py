import asyncio
from fastapi import FastAPI
from src.routers.lamoda import router
from src.routers.twitch import router_twitch
from producer import run_parser_lamoda, run_parser_twitch

app = FastAPI()

app.include_router(router)
app.include_router(router_twitch)
if __name__ == '__main__':
    run_parser_lamoda()
    run_parser_twitch()


