from typing import List, Dict
from fastapi import APIRouter, Body, HTTPException, status
from bson.objectid import ObjectId
from src.models.lamoda.models import Clothes, ClothesCreateUpdate, ClothesResponse
from src.models.database import lamoda_db

router = APIRouter(prefix='/lamoda')


@router.get('/clothes', response_model=ClothesResponse)
def get_clothes():
    return ClothesResponse(clothes=list(lamoda_db.find()))


@router.post("/create")
def create_thing(thing: ClothesCreateUpdate = Body(...)):
    new_thing = lamoda_db.insert_one(thing.dict())
    return {"_id": str(new_thing.inserted_id), **thing.dict()}


@router.delete("/{_id}")
async def delete_thing(_id: str):
    data = lamoda_db.find_one({'_id': ObjectId(_id)})
    if data:
        lamoda_db.find_one_and_delete({"_id": ObjectId(_id)})
        return {"message": f"Thing with ID {_id} was deleted"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Thing with ID {_id} not found')

