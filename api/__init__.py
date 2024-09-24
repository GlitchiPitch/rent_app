from fastapi import APIRouter

from core.config import settings
from .v1 import ads_router, user_router
from .authentication import router as auth_router

main_router = APIRouter(
    prefix=settings.api.prefix
)

main_router.include_router(ads_router)
main_router.include_router(auth_router)
main_router.include_router(user_router)