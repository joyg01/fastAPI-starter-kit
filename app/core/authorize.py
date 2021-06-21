"""
used to authorize each API call + decode open_token and get user's information
"""

from fastapi import Cookie, Depends, HTTPException, status
from app.core.config import settings, response_messages
from fastapi.security.http import HTTPBearer, HTTPAuthorizationCredentials
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBearer()

def unauthorized():
    """ just a common funtion to handle unauthoried exceptions

    Raises:
        HTTPException: return the user a json response with status code
    """
    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = response_messages.UNAUTHORIZED
    )


def bad_request(msg):
    """ just a common funtion to handle bad requests like not passing the token

    Raises:
        HTTPException: return the user a json response with status code
    """
    print("BAD REQUEST")
    raise HTTPException(
        status_code = status.HTTP_400_BAD_REQUEST,
        detail = str(msg)
    )


def validate_access_token(token)-> dict:
    try:
        validate_resp = requests.post(
            url=settings.OAUTH_VALIDATE_URL,
            params={
                "grant_type": "urn:pingidentity.com:oauth2:grant_type:validate_bearer",
                "token": token
            },
            auth=HTTPBasicAuth(settings.OAUTH_CLIENT_ID, settings.OAUTH_CLIENT_SECRET)
        )
        print("validate_resp: ", validate_resp)

        if validate_resp.status_code == 400:
            print("400")
            raise Exception("Invalid token")
        user_data = clean_up_token_data(validate_resp)
        return user_data
    except Exception as e:
        print(e)
        bad_request(str(e))

def clean_up_token_data(validate_resp):
    user_data = {}
    resp_json = validate_resp.json()
    user_data = resp_json["access_token"]
    print(user_data)
    # user_data["raw"] = resp_json
    return user_data


def get_user_data(access_token:HTTPAuthorizationCredentials  = Depends(auth)):
    if not (access_token.scheme == "Bearer" and access_token.credentials):
        bad_request("bearer token not found")

    print("access_token.scheme: ", access_token.scheme)
    print("access_token.credentials: ", access_token.credentials)
    user_data = validate_access_token(access_token.credentials)
    user_data["group"] = user_data.get("group", None)
    return user_data


def is_user_in_admin_group(user_data: dict = Depends(get_user_data)):
    """ This checks whether a user is part of the admin group

    Args:
        user_data (dict): a dict containing the decoded information
        from the open_token cookie

    Returns:
        user_data: this returned data is used by the apis for further processing
    """
    if settings.ADMIN_GROUP not in user_data["group"]:
        unauthorized()
    print("You are an authorized user: admin")
    return user_data


def is_user_in_permitted_group(user_data: dict = Depends(get_user_data)):
    """ This checks whether a user is part of the common user group

    Args:
        user_data (dict): a dict containing the decoded information
        from the open_token cookie

    Returns:
        user_data: this returned data is used by the apis for further processing
    """
    if settings.USER_GROUP not in user_data["group"]:
        unauthorized()
    return user_data


