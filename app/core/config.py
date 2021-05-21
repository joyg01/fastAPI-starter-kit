from pydantic import BaseSettings

class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    PROJECT_NAME: str = "Default App"
    PROJECT_VERSION: str = "0.1.0"
    API_V1_STR: str = f"{API_PREFIX}/v1"

    # DOCUMENTATIONS
    DOCUMENTATION: str = f"{API_PREFIX}/docs"
    READ_DOCUMENTATION: str = f"{API_PREFIX}/redocs"
    OPENAPI_URL: str = f"{API_V1_STR}/openapi.json"

    # FROM ENV
    OPEN_TOKEN_PASSWORD: str
    OPEN_TOKEN_NAME: str
    # USER GROUPS
    ADMIN_GROUP: str
    USER_GROUP: str

class ResponseMessages():
    UNAUTHORIZED: str = "You are not authorized to view this resource"
    TOKEN_ISSUE: str = "Seems there is some issue with the token provided"

settings = Settings()
response_messages = ResponseMessages()
