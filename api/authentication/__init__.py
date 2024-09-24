from fastapi import APIRouter, Depends

from api.authentication.user_manager import fastapi_users, current_active_user, auth_backend
from core.config import settings
from core.models.database import User
from core.schemas import UserUpdate, UserCreate, UserRead

router = APIRouter(
    prefix=settings.api.auth,
    tags=['Auth']
)

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
# router.include_router(
#     fastapi_users.get_users_router(UserRead, UserUpdate),
#     prefix="/users",
#     tags=["users"],
# )

@router.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}

#
# @app.on_event("startup")
# async def on_startup():
#     # Not needed if you setup a migration system like Alembic
#     await create_db_and_tables()