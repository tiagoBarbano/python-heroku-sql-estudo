from typing import Any
from app import service, cache
from fastapi_utils.tasks import repeat_every
from fastapi import FastAPI

def create_app():
    app: Any = FastAPI(
            title="Estudo Python SQL Heroku",
            description="Estudo Python SQL Heroku",
            version="1.0.0",
            openapi_url="/openapi.json",
            docs_url="/docs",
            redoc_url="/redoc"
          )

    @app.on_event('startup')
    @repeat_every(seconds=60 * 60)  
    async def startup_event():
        await cache.init_cache_user()
    
    app.include_router(service.router, prefix="/v1/user", tags=["Users"])
    #app.include_router(cache.router, prefix="/v1/cache", tags=["cache"])

    return app
