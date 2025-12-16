"""
Weather service module containing business logic.
This demonstrates how to organize service/business logic layer.
"""

from typing import Any, Dict, List
from datetime import datetime, timezone

# Import from core configuration module (example of cross-module import)
from app.core.config import settings


class WeatherService:
    """
    Service class for weather-related business logic.
    This is dummy logic to demonstrate proper module organization.
    """

    def __init__(self):
        """Initialize the weather service with some dummy data."""
        self._weather_data = {
            "New York": {"temp": 72.5, "humidity": 65, "condition": "Partly Cloudy"},
            "London": {"temp": 59.0, "humidity": 78, "condition": "Rainy"},
            "Tokyo": {"temp": 68.3, "humidity": 55, "condition": "Sunny"},
            "Sydney": {"temp": 77.9, "humidity": 60, "condition": "Clear"},
        }

    def get_weather(self, city: str) -> Dict[str, Any]:
        """
        Get weather information for a specific city.

        Args:
            city: Name of the city

        Returns:
            Dictionary containing weather information

        Raises:
            ValueError: If city is not found
        """
        weather = self._weather_data.get(city)

        if not weather:
            raise ValueError(f"Weather data not found for city: {city}")

        # Use config to validate temperature (example of using config in service)
        if weather["temp"] > settings.max_temperature:
            weather["warning"] = "Temperature exceeds maximum threshold!"

        # Add metadata
        weather["timestamp"] = datetime.now(timezone.utc).isoformat()
        weather["city"] = city

        return weather

    def get_available_cities(self) -> List[str]:
        """
        Get list of cities with available weather data.

        Returns:
            List of city names
        """
        return list(self._weather_data.keys())

    def calculate_heat_index(self, temperature: float, humidity: float) -> float:
        """
        Calculate heat index (dummy calculation for demonstration).

        Args:
            temperature: Temperature in Fahrenheit
            humidity: Humidity percentage

        Returns:
            Calculated heat index
        """
        # Simplified dummy calculation
        heat_index = temperature + (0.5 * humidity)
        return round(heat_index, 2)


# Create a singleton instance that can be imported
weather_service = WeatherService()
