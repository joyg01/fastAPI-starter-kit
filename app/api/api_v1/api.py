from fastapi import APIRouter

from app.api.api_v1.endpoints import root, admin, user

api_router = APIRouter()
api_router.include_router(root.router)
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(admin.router, prefix="/admin", tags=["admin"])

