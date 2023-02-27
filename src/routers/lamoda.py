from fastapi import APIRouter, Body, Depends
from src.models.lamoda.models import Clothes, ClothesCreateUpdate, ClothesResponse
from src.di.lamoda_di import LamodaService

router = APIRouter(prefix='/lamoda')


@router.get('/clothes', response_model=ClothesResponse)
def get_clothes(service: LamodaService = Depends()):
    return service.get_all_clothes()


@router.post("/create")
def create_thing(thing: ClothesCreateUpdate = Body(...), service: LamodaService = Depends()):
    return service.create_thing_lamoda(thing)


@router.delete("/{_id}")
def delete_thing(_id: str, service: LamodaService = Depends()):
    return service.delete_thing(_id)


@router.get('/{_id}', response_model=Clothes)
def get_thing(_id: str, service: LamodaService = Depends()):
    return service.get_one_thing(_id)
