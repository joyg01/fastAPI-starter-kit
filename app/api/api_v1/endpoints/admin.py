from fastapi import APIRouter, Depends
from app.core.authorize import is_user_in_admin_group

router = APIRouter()

@router.get("/whoami")
def root(user_info: dict = Depends(is_user_in_admin_group)):
    return user_info