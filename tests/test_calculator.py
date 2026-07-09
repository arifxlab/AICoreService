from .conftest import client


def test_calculator():
    response = client.post(
        "/api/v1/chat",
        json={
            "system_prompt": "",
            "user_prompt": "calc: 5*5",
            "model": "google/gemma-3-27b-it",
            "temperature": 0,
            "max_tokens": 10,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["content"] == "25"
