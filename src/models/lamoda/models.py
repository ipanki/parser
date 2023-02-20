from typing import Optional, List
from pydantic import BaseModel, Field, validator
from datetime import datetime
from bson.objectid import ObjectId
from src.models.validators import object_id_to_string


class Clothes(BaseModel):
    id: str = Field(..., alias="_id")
    brand: str = Field(...)
    model: str = Field(...)
    category: str = Field(...)
    price: str = Field(...)
    created_at: datetime | datetime.utcnow()

    @validator('id', pre=True)
    def validate_id(cls, _id) -> str:
        return object_id_to_string(_id)

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example': {
                'id': '729f2221872934bd5f762fff',
                'brand': 'Puma',
                'model': 'Брюки спортивные ACTIVE Tricot Pants cl',
                'category': 'Кроссовки',
                'price': '250.00',
                'created_at': '2022-09-21T09:33:06Z'
            }
        }


class ClothesCreateUpdate(BaseModel):
    brand: Optional[str]
    model: Optional[str]
    category: Optional[str]
    price: Optional[str]

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example': {
                'brand': 'Puma',
                'model': 'Брюки спортивные ACTIVE Tricot Pants cl',
                'category': 'Брюки',
                'price': '255.00'
            }
        }


class ClothesResponse(BaseModel):
    clothes: List[Clothes]
