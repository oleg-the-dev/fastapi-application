from fastapi.testclient import TestClient

from app.core.config import settings
from app.tests.utils import get_random_values


def test_create_with_invalid_values(client: TestClient):
    # Invalid username
    json = {'username': '', 'password': 'password', 'role_id': 1}
    response = client.post('/users', json=json)
    assert response.status_code == 422

    # Invalid password
    json = {'username': 'username', 'password': '', 'role_id': 1}
    response = client.post('/users', json=json)
    assert response.status_code == 422

    # Invalid role_id
    json = {'username': 'username', 'password': 'password', 'role_id': '0'}
    response = client.post('/users', json=json)
    assert response.status_code == 422


def test_create_user(client: TestClient):
    json = get_random_values()
    response = client.post(
        '/users',
        json=json
    )
    assert response.status_code == 201
    assert response.json() == {'username': json['username'],
                               'role_id': json['role_id']}


def test_create_existing_user(client: TestClient):
    response = client.post(
        '/users',
        json={
            'username': settings.TEST_USER_USERNAME,
            'password': settings.TEST_USER_PASSWORD,
            'role_id': settings.TEST_USER_ROLE_ID,
        },
    )
    assert response.status_code == 400
    assert response.json() == {'detail': settings.INVALID_USERNAME}
