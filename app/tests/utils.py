import random
import string
from typing import Dict

from fastapi.testclient import TestClient

from app.core.config import settings


def get_random_values() -> dict:
    values = string.ascii_letters + string.digits
    username = ''.join(random.choices(values, k=12))
    password = ''.join(random.choices(values, k=8))
    role_id = random.choice([1, 2])
    json = {
        'username': username,
        'password': password,
        'role_id': role_id,
    }
    return json


def get_user_token_headers(client: TestClient) -> Dict[str, str]:
    login_data = {
        "username": settings.TEST_USER_USERNAME,
        "password": settings.TEST_USER_PASSWORD,
    }
    r = client.post('/auth/access-token', data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers
