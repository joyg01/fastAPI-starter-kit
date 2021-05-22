"""
used to authorize each API call + decode open_token and get user's information
"""

from fastapi import Cookie, Depends, HTTPException, status
from opentoken import OpenToken
from app.core.config import settings, response_messages


def decode_open_token(open_token: str = Cookie(None)):
    """ to decode the open_token passed.
    This uses a custome open_token library suitable for pfizers needs

    Args:
        open_token (str): cookie is decodes and used for validation of group
        as well as get users information.

    Returns:
        user_data: for further processing like checking the user groups
    """
    if not open_token:
        unauthorized()
    try:
        token = OpenToken(settings.OPEN_TOKEN_PASSWORD)
        user_data= token.parse_token(open_token)
        return user_data
    except Exception as e:
        print(e)
        bad_request(e)


def is_user_in_admin_group(user_data: dict = Depends(decode_open_token)):
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


def is_user_in_permitted_group(user_data: dict = Depends(decode_open_token)):
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
    raise HTTPException(
        status_code = status.HTTP_400_BAD_REQUEST,
        detail = str(msg)
    )
