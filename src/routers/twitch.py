from fastapi import APIRouter, Body, Depends
from fastapi_redis_cache import cache
from src.models.twtich.models import Streams, StreamsCreateUpdate, StreamsResponse
from src.di.twitch_di import TwitchService

router_twitch = APIRouter(prefix='/twitch')


@router_twitch.get('/streams', response_model=StreamsResponse)
@cache(expire=1)
def get_streams(service: TwitchService = Depends()):
    return service.get_all_streams()


@router_twitch.post("/create")
def create(stream: StreamsCreateUpdate = Body(...), service: TwitchService = Depends()):
    return service.create_stream(stream)


@router_twitch.delete("/{_id}")
def delete(_id: str, service: TwitchService = Depends()):
    return service.delete_stream(_id)


@router_twitch.get('/{_id}', response_model=Streams)
@cache(expire=1)
def get_one_stream(_id: str, service: TwitchService = Depends()):
    return service.get_one_stream(_id)
