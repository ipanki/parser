import asyncio
from fastapi import FastAPI, Request, Response
from fastapi_redis_cache import FastApiRedisCache, cache
from src.routers.lamoda import router
from src.routers.twitch import router_twitch
from producer import run_parser_lamoda, run_parser_twitch
from src.config.config import config

app = FastAPI()

app.include_router(router)
app.include_router(router_twitch)


@app.on_event("startup")
def startup():
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=config.LOCAL_REDIS_URL,
        prefix="api-cache",
        response_header="X-API-Cache"
    )


if __name__ == '__main__':
    run_parser_lamoda()
    run_parser_twitch()


