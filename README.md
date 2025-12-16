# Weather API - FastAPI Template Project

A modern, production-ready FastAPI template with proper project structure, demonstrating best practices for organizing modules, imports, testing, and containerization.

## Project Structure

```text
weather/
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── weather.py         # API route handlers
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py              # Configuration management
│   └── services/
│       ├── __init__.py
│       └── weather_service.py     # Business logic layer
├── tests/
│   ├── __init__.py
│   ├── conftest.py                # Pytest fixtures
│   └── test_weather.py            # API tests
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Multi-stage Docker build
├── docker-compose.yml             # Docker Compose configuration
├── .dockerignore                  # Docker ignore rules
└── README.md                      # This file
```

## Key Features

### Proper Module Organization

- **Nested package structure** demonstrating proper Python imports
- **Separation of concerns**: routes, services, and configuration
- **Absolute imports** from the `app` package root

### Import Examples

The project demonstrates how to import from nested modules:

```python
# From routes importing services (app/api/routes/weather.py)
from app.services.weather_service import weather_service
from app.core.config import settings

# From main app importing routes (app/main.py)
from app.api.routes import weather

# In tests importing the app (tests/test_weather.py)
from app.main import app
from app.services.weather_service import weather_service
```

### Modern FastAPI Practices

- **Pydantic Settings** for configuration management
- **Router organization** for modular API endpoints
- **Dependency injection** ready structure
- **Type hints** throughout the codebase
- **API documentation** with OpenAPI/Swagger

### Testing with Pytest

- **Test fixtures** in conftest.py
- **TestClient** for endpoint testing
- **Parametrized tests** for comprehensive coverage
- **Service layer testing** examples

### Docker Support

- **Multi-stage build** for optimized image size
- **Non-root user** for security
- **Health checks** configured
- **Docker Compose** for easy deployment

## Getting Started

### Local Development (without Docker)

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
# Option 1: Using uvicorn directly
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Option 2: Using Python module
python -m app.main
```

4. Run tests:

```bash
pytest
pytest -v  # verbose output
pytest --cov=app  # with coverage (requires pytest-cov)
```

### Docker Development

1. Build and run with Docker Compose:

```bash
docker-compose up --build
```

2. Run in detached mode:

```bash
docker-compose up -d
```

3. View logs:

```bash
docker-compose logs -f
```

4. Stop services:

```bash
docker-compose down
```

### Running Tests in Docker

```bash
# Build the image
docker build -t weather-api .

# Run tests
docker run --rm weather-api pytest
docker run --rm weather-api pytest -v
```

## API Endpoints

Once running, the API is available at `http://localhost:8000`

### Available Endpoints

- `GET /` - Root endpoint (health check)
- `GET /health` - Health check
- `GET /api/v1/weather/` - Get weather for a city (query param: `city`)
- `GET /api/v1/weather/cities` - List available cities
- `GET /api/v1/weather/heat-index` - Calculate heat index (query params: `temperature`, `humidity`)
- `GET /api/v1/weather/info` - API information

### Interactive Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Example API Calls

```bash
# Get weather for a city
curl "http://localhost:8000/api/v1/weather/?city=New%20York"

# List available cities
curl "http://localhost:8000/api/v1/weather/cities"

# Calculate heat index
curl "http://localhost:8000/api/v1/weather/heat-index?temperature=75&humidity=60"

# API info
curl "http://localhost:8000/api/v1/weather/info"
```

## Configuration

Configuration is managed through environment variables using Pydantic Settings.

Create a `.env` file in the root directory:

```env
APP_NAME=Weather API
DEBUG=true
API_VERSION=v1
MAX_TEMPERATURE=100.0
```

## Understanding the Import Structure

This project uses **absolute imports** from the `app` package:

1. **In route handlers** (`app/api/routes/weather.py`):
   - Import services: `from app.services.weather_service import weather_service`
   - Import config: `from app.core.config import settings`

2. **In main app** (`app/main.py`):
   - Import routers: `from app.api.routes import weather`

3. **In tests** (`tests/test_weather.py`):
   - Import app: `from app.main import app`
   - Import services: `from app.services.weather_service import weather_service`

**Why absolute imports?**

- Clear and unambiguous
- Works regardless of where Python is executed from
- Easier to refactor and maintain
- Standard practice for Python packages

## Package Versions (Latest as of January 2025)

- FastAPI: 0.115.6
- Uvicorn: 0.34.0
- Pydantic: 2.10.5
- Pytest: 8.3.4
- Python: 3.12

## Next Steps

To extend this template:

1. **Add a database**: Uncomment PostgreSQL in docker-compose.yml, add SQLAlchemy/Tortoise ORM
2. **Add authentication**: Implement JWT or OAuth2 in a new `app/core/security.py`
3. **Add more routes**: Create new route files in `app/api/routes/`
4. **Add models**: Create Pydantic models in `app/models/`
5. **Add middleware**: Add custom middleware in `app/middleware/`
6. **Add background tasks**: Use FastAPI background tasks or Celery
7. **Add caching**: Integrate Redis for caching

## Best Practices Demonstrated

- Proper Python package structure with `__init__.py`
- Absolute imports from package root
- Configuration management with Pydantic Settings
- Layered architecture (routes → services → core)
- Comprehensive testing with pytest
- Docker multi-stage builds
- Non-root Docker user for security
- Health checks for monitoring
- Type hints for better IDE support
- API documentation with OpenAPI

## License

This is a template project - use it however you like!
