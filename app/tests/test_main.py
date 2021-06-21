"""
used as a main entry point for pytest
"""

from fastapi.testclient import TestClient
from app.core.authorize import decode_open_token
from app.tests import overrides
from main import app

client = TestClient(app)

# overriding the open_token check
app.dependency_overrides[decode_open_token] = overrides.decoded_open_token
