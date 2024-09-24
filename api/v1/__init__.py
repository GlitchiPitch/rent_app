from fastapi import APIRouter

from core.config import settings
from core.schemas import AdAdd, AdShow

paths = settings.api.v1

router = APIRouter(
    prefix=paths.prefix
)

async def _get_all_ads():
    ...

#TODO how to show return for json
async def _new_ads(body: AdAdd):
    return {
        'status': 200,
        'message': AdShow(**body.model_dump())
    }
@router.get(paths.get_all_ads)
async def get_all_ads():
    ...

@router.post(paths.new_ads)
async def new_ads():
    ...

