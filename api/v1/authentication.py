from fastapi import APIRouter

from core.models.user_manager import fastapi_users, auth_backend
from core.config import settings
from core.schemas import UserCreate, UserRead

router = APIRouter(
    prefix=settings.api.auth,
    tags=['Auth']
)

# /login /logout
router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/jwt"
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)

router.include_router(
    fastapi_users.get_reset_password_router(),
)

router.include_router(
    fastapi_users.get_verify_router(UserRead),
)


