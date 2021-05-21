from fastapi import Cookie, Depends, HTTPException, status
from opentoken import OpenToken
from app.core.config import settings, response_messages


def decode_open_token(open_token: str = Cookie(None)):
    if not open_token:
        unauthorized()
    try:
        token = OpenToken(settings.OPEN_TOKEN_PASSWORD)
        user_data= token.parse_token(open_token)
        print("user_data", user_data)
        return user_data
    except Exception as e:
        print(e)
        bad_request(e)


def is_user_in_admin_group(user_data: dict = Depends(decode_open_token)):
    print("user_data", user_data)
    if settings.ADMIN_GROUP not in user_data["group"]:
        unauthorized()
    print("You are an authorized user: admin")
    return user_data


def is_user_in_permitted_group(user_data: dict = Depends(decode_open_token)):
    if settings.USER_GROUP not in user_data["group"]:
        unauthorized()
    return user_data


def unauthorized():
    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = response_messages.UNAUTHORIZED
    )


def bad_request(msg):
    raise HTTPException(
        status_code = status.HTTP_400_BAD_REQUEST,
        detail = str(msg)
    )
