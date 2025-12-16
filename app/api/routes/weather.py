"""
Weather API routes.
This demonstrates proper importing from nested service modules.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Any, Dict, List

# Example of importing from deeply nested module structure
# Note: We use absolute imports starting from 'app'
from app.services.weather_service import weather_service
from app.core.config import settings

# Create a router instance
router = APIRouter(
    prefix="/weather",
    tags=["weather"],
)


@router.get("/", response_model=Dict[str, Any])
async def get_weather(
    city: str = Query(
        ...,
        description="Name of the city to get weather for",
        examples=["New York", "London", "Tokyo"]
    )
) -> Dict[str, Any]:
    """
    Get current weather for a specific city.

    This is the main GET route demonstrating:
    - Proper import from services module
    - Query parameter validation
    - Error handling
    - Response model typing

    Args:
        city: Name of the city

    Returns:
        Weather information dictionary

    Raises:
        HTTPException: 404 if city not found
    """
    try:
        # Call the service layer (imported from app.services.weather_service)
        weather_data = weather_service.get_weather(city)
        return weather_data
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/cities", response_model=List[str])
async def get_available_cities() -> List[str]:
    """
    Get list of cities with available weather data.

    Returns:
        List of city names
    """
    return weather_service.get_available_cities()


@router.get("/heat-index", response_model=Dict[str, float])
async def calculate_heat_index(
    temperature: float = Query(..., description="Temperature in Fahrenheit", ge=-50, le=150),
    humidity: float = Query(..., description="Humidity percentage", ge=0, le=100)
) -> Dict[str, float]:
    """
    Calculate heat index from temperature and humidity.

    Demonstrates:
    - Using service layer methods
    - Query parameter validation with constraints

    Args:
        temperature: Temperature in Fahrenheit
        humidity: Humidity percentage

    Returns:
        Dictionary with heat index value
    """
    heat_index = weather_service.calculate_heat_index(temperature, humidity)
    return {
        "temperature": temperature,
        "humidity": humidity,
        "heat_index": heat_index
    }


@router.get("/info", response_model=Dict[str, str])
async def get_api_info() -> Dict[str, str]:
    """
    Get API information.

    Demonstrates importing and using configuration from app.core.config

    Returns:
        API information dictionary
    """
    return {
        "app_name": settings.app_name,
        "version": settings.api_version,
        "debug_mode": str(settings.debug),
    }
