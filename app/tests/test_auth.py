from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_access_token(client: TestClient):
    login_data = {
        'username': settings.TEST_USER_USERNAME,
        'password': settings.TEST_USER_PASSWORD,
    }
    response = client.post(
        '/auth/access-token',
        data=login_data,
    )
    tokens = response.json()
    assert response.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]


def test_auth_with_invalid_values(client: TestClient):
    login_data = {
        'username': 'idontexist',
        'password': 'idontexist',
    }
    response = client.post(
        '/auth/access-token',
        data=login_data,
    )
    assert response.status_code == 400

    login_data['username'] = settings.TEST_USER_USERNAME
    response = client.post(
        '/auth/access-token',
        data=login_data,
    )
    assert response.status_code == 400
