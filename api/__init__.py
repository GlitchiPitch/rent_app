from fastapi import APIRouter

from core.config import settings
from .v1 import router as api_v1_router

main_router = APIRouter(
    prefix=settings.api.prefix
)

main_router.include_router(api_v1_router)