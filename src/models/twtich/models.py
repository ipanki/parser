from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field, validator
from bson.objectid import ObjectId
from src.models.validators import object_id_to_string


class Streams(BaseModel):
    id: str = Field(..., alias="_id")
    game: str = Field(...)
    title: str = Field(...)
    user_login: str = Field(...)
    user_name: str = Field(...)
    viewer_count: int = Field(...)
    type: str = Field(...)
    created_at: datetime = datetime.utcnow()

    @validator('id', pre=True)
    def validate_id(cls, v) -> str:
        return object_id_to_string(v)

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example': {
                'id': '62f264f7705d3742932262ec',
                'game_': 'Counter-Strike: Global Offensive',
                'title': 'Hard stream',
                'type': 'live',
                'user_login': 'RazDva',
                'user_name': 'RAZDVA',
                'viewer_count': 7777,
                'created_at': '2022-09-21T09:33:06Z'
            }
        }


class StreamsResponse(BaseModel):
    streams: List[Streams]


class StreamsCreateUpdate(BaseModel):
    game: Optional[str]
    title: Optional[str]
    user_login: Optional[str]
    user_name: Optional[str]
    viewer_count: Optional[int]
    type: Optional[str]

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example': {
                'game': 'Dota 2',
                'title': 'Zhestko',
                'type': 'live',
                'user_login': 'DvaRaz',
                'user_name': 'DvaRaz',
                'viewer_count': 7777
            }
        }