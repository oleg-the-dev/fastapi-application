from fastapi.testclient import TestClient


def test_unauthenticated_client(client: TestClient):
    response = client.post(
        '/items/1/buy',
    )
    assert response.status_code == 401

    response = client.post(
        '/items/1/sell',
    )
    assert response.status_code == 401


def test_buy_item(client: TestClient, user_token_headers):
    '''
    Test user has «buyer» role so it should not give any errors.
    '''
    response = client.post(
        '/items/1/buy',
        json={'quantity': 0},
        headers=user_token_headers,
    )
    assert response.status_code == 200


def test_sell_item(client: TestClient, user_token_headers):
    '''
    Test user has «buyer» role so it should give error 403 «Forbidden» when
    user tries to sell something.
    '''
    response = client.post(
        '/items/1/sell',
        json={'quantity': 0},
        headers=user_token_headers,
    )
    assert response.status_code == 403


def test_item_does_not_exist(client: TestClient, user_token_headers):
    response = client.post(
        '/items/0/sell',
        json={'quantity': 0},
        headers=user_token_headers,
    )
    assert response.status_code == 404
