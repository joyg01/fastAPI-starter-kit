from fastapi import Cookie, HTTPException, status
from app.tests.test_config import test_settings

# this overrides the OPEN_TOKEN decoding
def decoded_open_token(open_token: str = Cookie(None)):
    if not open_token:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
        )
    # returns a decodes token as if the decoding was successful
    return test_settings.OPEN_TOKEN_DECODED_USER