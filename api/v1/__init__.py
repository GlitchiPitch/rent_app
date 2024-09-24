__all__ = (
    'ads_router',
    'user_router',
    'auth_router'
)

from .user import router as user_router
from .ads import router as ads_router
from .authentication import router as auth_router