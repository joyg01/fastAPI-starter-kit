"""
used for testing the user's access
"""

from app.core.config import settings
from app.tests.test_config import test_settings

from app.tests.test_main import client

# common routes for user
API_URL = f"{settings.API_SERVER_URL}:{settings.API_SERVER_PORT}{settings.API_V1_STR}"

# setting dummy open_token
client.cookies["open_token"] = test_settings.OPEN_TOKEN_DUMMY

# used to test if the user is part of the permitted common user group
def test_user_group_access() -> None:
    r = client.get(f"{API_URL}{settings.API_USER_PREFIX}/whoami")
    assert r.status_code == 200
