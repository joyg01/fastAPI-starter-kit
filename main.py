from fastapi import FastAPI
from app.core.config import settings
from app.api.api_v1.api import api_router

app = FastAPI(
    title = settings.PROJECT_NAME,
    docs_url = settings.DOCUMENTATION,
    redoc_url = settings.READ_DOCUMENTATION,
    openapi_url = settings.OPENAPI_URL
)

# all routes included here
app.include_router(api_router, prefix=settings.API_V1_STR)
