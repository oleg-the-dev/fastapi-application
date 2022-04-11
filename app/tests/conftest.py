import pytest
from typing import Generator

from fastapi.testclient import TestClient

from app.core.dependencies import get_db
from app.database.db import TestSessionLocal
from app.tests.utils import get_user_token_headers
from main import app


@pytest.fixture
def session() -> Generator:
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session) -> Generator:
    def override_get_db():
        try:
            db = session
            yield db
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c


@pytest.fixture
def user_token_headers(client: TestClient):
    return get_user_token_headers(client)
