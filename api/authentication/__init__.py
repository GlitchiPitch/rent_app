from fastapi import APIRouter, Depends

from api.authentication.user_manager import fastapi_users, current_active_user, auth_backend
from core.config import settings
from core.models.database import User
from core.schemas import UserUpdate, UserCreate, UserRead

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


