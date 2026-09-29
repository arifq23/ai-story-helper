from unittest.mock import patch
from fastapi.testclient import TestClient
from unittest.mock import patch

from api import app
from api import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }

def test_analyse_story_endpoint():
    response = client.post(
        "/analyse-story",
        json={
            "story": (
                "As a product owner, "
                "I want to assess a COBOL application "
                "so that I can understand its migration complexity."
            )
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["analysis"]["role"] == "product owner"
    assert data["analysis"]["goal"] == "to assess a COBOL application"
    assert data["analysis"]["score"] == 3
    assert data["analysis"]["is_valid"] is True


def test_analyse_story_missing_story_field():
    response = client.post(
        "/analyse-story",
        json={
            "description": "Assess a COBOL application"
        }
    )

    assert response.status_code == 422

    data = response.json()

    assert "detail" in data
    assert data["detail"][0]["loc"] == ["body", "story"]

def test_enhance_story_endpoint():
    fake_ai_result = {
        "status": "success",
        "message": {
            "improved_story": "Improved test story",
            "suggestions": ["Add more business context"],
            "acceptance_criteria": ["Application can be assessed"],
            "edge_cases": ["Application contains unsupported code"]
        },
        "original_story": "Test story"
    }

    with patch("api.enhance_story_with_ai", return_value=fake_ai_result):
        response = client.post(
            "/enhance-story",
            json={
                "story": "Test story"
            }
        )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["enhancement"]["improved_story"] == "Improved test story"


def test_enhance_story_ai_failure():
    fake_ai_result = {
        "status": "error",
        "message": "Upstream AI service unavailable",
        "original_story": "Test story"
    }

    with patch("api.enhance_story_with_ai", return_value=fake_ai_result):
        response = client.post(
            "/enhance-story",
            json={
                "story": "Test story"
            }
        )

    assert response.status_code == 502

    data = response.json()

    assert data["detail"] == "Upstream AI service unavailable"