from typing import Annotated, TYPE_CHECKING
from fastapi import APIRouter, Depends

from sqlalchemy import select, and_, delete

from core.models import User, Ad
from core.models.user_manager import current_active_user
from core.config import settings
from core.models.database import get_async_session
from core.schemas import AdCreate, AdShow

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

paths = settings.api.v1

router = APIRouter(
    prefix=paths.prefix,
    tags=['Ads']
)

# TODO how to show return for json
# TODO make a superuser with ids of ads
# TODO how to make delete user and logout after that

NewAdDep = Annotated[AdCreate, Depends()]
UserDep = Annotated[User, Depends(current_active_user)]
SessionDep = Annotated['AsyncSession', Depends(get_async_session)]

@router.get(paths.get_all_ads)
async def get_all_ads(user: UserDep, session: SessionDep) -> list[AdShow]:
    stmt = select(Ad).where(Ad.user_id == user.id)
    res = await session.execute(stmt)
    res = [
        AdShow(
            room_count=ad.room_count,
            cost=ad.cost,
            address=ad.address,
        ) for ad in res.scalars().all()
    ]
    return res

@router.get(paths.get_one)
async def get_one_ad(id: int, user: UserDep, session: SessionDep) -> AdShow:
    stmt = select(Ad).where(and_(Ad.id == id, Ad.user_id == user.id))
    result = await session.execute(stmt)
    result = result.fetchone()[0]
    return AdShow(
        room_count=result.room_count,
        cost=result.cost,
        address=result.address,
    )

@router.post(paths.new_ad)
async def add_new_ad(body: NewAdDep, user: UserDep, session: SessionDep) -> AdShow:
    new_ad = Ad(
        user_id=user.id,
        **body.model_dump()
    )
    session.add(new_ad)
    await session.commit()
    return AdShow(**body.model_dump())

@router.delete(paths.delete_ad)
async def delete_ad(id: int, user: UserDep, session: SessionDep):
    stmt = select(Ad).where(and_(Ad.id == id, Ad.user_id == user.id))
    result = await session.execute(stmt)
    result = result.scalars().all()
    if len(result) > 0:
        deleted_ad = result[0]
        stmt = delete(Ad).where(and_(Ad.id == id, Ad.user_id == user.id))
        await session.execute(stmt)
        await session.commit()
        return AdShow(
            room_count=deleted_ad.room_count,
            cost=deleted_ad.cost,
            address=deleted_ad.address,
        )
    else:
        return {
            'status': 404,
            'message': "Ad not found"
        }
