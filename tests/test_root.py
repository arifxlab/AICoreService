from .conftest import client


def test_root():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert "message" in data
