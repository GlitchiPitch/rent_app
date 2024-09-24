from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models.database import get_async_session
from .v1 import ads_router, user_router, auth_router

main_router = APIRouter(
    prefix=settings.api.prefix
)

main_router.include_router(ads_router)
main_router.include_router(auth_router)
main_router.include_router(user_router)

@main_router.get('')
async def get_all_users(session: Annotated[AsyncSession, Depends(get_async_session)]):
    return