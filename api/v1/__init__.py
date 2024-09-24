from fastapi import APIRouter

from core.config import settings

paths = settings.api.v1

router = APIRouter(
    prefix=paths.prefix
)

