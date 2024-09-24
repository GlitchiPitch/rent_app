from typing import Annotated

from fastapi import APIRouter, Depends

from core.models.user_manager import current_active_user

from core.config import settings
from core.models.database import User
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


NewAdDep = Annotated[AdAdd, Depends()]
UserDep = Annotated[User, Depends(current_active_user)]
DeleteAdDep = Annotated[dict, Depends(_delete_ad)]

def _get_all_ads():
    return {
        'status': 200,
        'message': True
    }

@router.get(paths.get_all_ads)
async def get_all_ads(user: UserDep):
    return _get_all_ads()

@router.post(paths.new_ad)
async def new_ad(body: NewAdDep, user: UserDep) -> AdShow:
    return AdShow(**body.model_dump())

@router.delete(paths.delete_ad)
async def delete_ad(body: DeleteAdDep, user: UserDep):
    return body
