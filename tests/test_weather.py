"""
Tests for weather API endpoints.
Demonstrates pytest best practices for FastAPI testing.
"""

import pytest
from fastapi.testclient import TestClient


def test_root_endpoint(client: TestClient):
    """Test the root endpoint returns correct response."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert data["version"] == "v1"


def test_health_check(client: TestClient):
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_get_weather_valid_city(client: TestClient):
    """Test getting weather for a valid city."""
    response = client.get("/api/v1/weather/?city=New York")
    assert response.status_code == 200
    data = response.json()
    assert data["city"] == "New York"
    assert "temp" in data
    assert "humidity" in data
    assert "condition" in data
    assert "timestamp" in data


def test_get_weather_invalid_city(client: TestClient):
    """Test getting weather for an invalid city returns 404."""
    response = client.get("/api/v1/weather/?city=InvalidCity")
    assert response.status_code == 404
    assert "detail" in response.json()


def test_get_available_cities(client: TestClient):
    """Test getting list of available cities."""
    response = client.get("/api/v1/weather/cities")
    assert response.status_code == 200
    cities = response.json()
    assert isinstance(cities, list)
    assert len(cities) > 0
    assert "New York" in cities


def test_calculate_heat_index(client: TestClient):
    """Test heat index calculation endpoint."""
    response = client.get("/api/v1/weather/heat-index?temperature=75&humidity=60")
    assert response.status_code == 200
    data = response.json()
    assert "heat_index" in data
    assert data["temperature"] == 75
    assert data["humidity"] == 60


def test_calculate_heat_index_invalid_params(client: TestClient):
    """Test heat index with invalid parameters."""
    # Temperature too high
    response = client.get("/api/v1/weather/heat-index?temperature=200&humidity=60")
    assert response.status_code == 422  # Validation error

    # Humidity out of range
    response = client.get("/api/v1/weather/heat-index?temperature=75&humidity=150")
    assert response.status_code == 422


def test_get_api_info(client: TestClient):
    """Test API info endpoint."""
    response = client.get("/api/v1/weather/info")
    assert response.status_code == 200
    data = response.json()
    assert "app_name" in data
    assert "version" in data
    assert data["app_name"] == "Weather API"


# Example of testing the service layer directly
def test_weather_service_import():
    """Test that we can import and use the weather service directly."""
    from app.services.weather_service import weather_service

    cities = weather_service.get_available_cities()
    assert isinstance(cities, list)
    assert len(cities) > 0


def test_weather_service_heat_index():
    """Test heat index calculation in service layer."""
    from app.services.weather_service import weather_service

    heat_index = weather_service.calculate_heat_index(75.0, 60.0)
    assert isinstance(heat_index, float)
    assert heat_index > 0


# Example of parametrized testing
@pytest.mark.parametrize("city", ["New York", "London", "Tokyo", "Sydney"])
def test_all_cities_have_weather(client: TestClient, city: str):
    """Test that all available cities return valid weather data."""
    response = client.get(f"/api/v1/weather/?city={city}")
    assert response.status_code == 200
    data = response.json()
    assert data["city"] == city
    assert "temp" in data
