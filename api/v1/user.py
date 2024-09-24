from fastapi import APIRouter, Depends

from api.authentication import fastapi_users, current_active_user
from core.config import settings
from core.models.database import User
from core.schemas import UserUpdate, UserRead

router = APIRouter(
    prefix=settings.api.user,
    tags=["Users"],
)

# /me
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
)

@router.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}