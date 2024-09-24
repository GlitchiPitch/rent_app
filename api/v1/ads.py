from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from core.config import settings
from core.schemas import AdAdd, AdShow

paths = settings.api.v1

router = APIRouter(
    prefix=paths.prefix,
    tags=['Ads']
)

# TODO how to show return for json

def _delete_ad(
    ad_id: int
):
    return {
        'status': 200,
        'message': f'ad with id {ad_id} was deleted'
    }

NewAdDep = Annotated[AdShow, Depends()]
DeleteAdDep = Annotated[dict, Depends(_delete_ad)]

def _get_all_ads():
    return {
        'status': 200,
        'message': True
    }

@router.get(paths.get_all_ads)
async def get_all_ads():
    return _get_all_ads()

@router.post(paths.new_ad)
async def new_ad(body: NewAdDep):
    return body

@router.delete(paths.delete_ad)
async def delete_ad(body: DeleteAdDep):
    return body
