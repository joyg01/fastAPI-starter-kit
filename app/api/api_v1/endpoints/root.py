from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {
        "Hello": "from root router"
    }