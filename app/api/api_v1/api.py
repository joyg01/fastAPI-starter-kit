from fastapi import APIRouter
from app.core.config import settings
from app.api.api_v1.endpoints import root, admin, user

api_router = APIRouter()
api_router.include_router(root.router)
api_router.include_router(user.router, prefix=settings.API_USER_PREFIX, tags=["user"])
api_router.include_router(admin.router, prefix=settings.API_ADMIN_PREFIX, tags=["admin"])

