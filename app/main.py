"""
Main FastAPI application.
This is the entry point that ties all modules together.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import router from nested routes module
# This demonstrates importing from app.api.routes.weather
from app.api.routes import weather
from app.core.config import settings

# Create FastAPI application instance
app = FastAPI(
    title=settings.app_name,
    version=settings.api_version,
    debug=settings.debug,
    docs_url="/docs",
    redoc_url="/redoc",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers from api.routes module
# This shows how to organize routes in separate modules
app.include_router(weather.router, prefix="/api/v1")


@app.get("/")
async def root():
    """
    Root endpoint - simple health check.

    This is the minimal GET route requested.
    For more complex routes, see /api/v1/weather endpoints.

    Returns:
        Simple welcome message
    """
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": settings.api_version,
        "docs": "/docs",
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring.

    Returns:
        Health status
    """
    return {"status": "healthy"}


# This allows running with `python -m app.main` for development
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=settings.debug)
