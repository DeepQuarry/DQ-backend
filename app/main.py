from fastapi import FastAPI

from app.api.v1.api import main_router
from app.core.config import settings
from app.core.log import generate_logger

logger = generate_logger()
logger.info("Starting API")

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# add middleware, origins here


app.include_router(main_router, prefix=settings.API_V1_STR)


@app.get("/")
async def main():
    return {"message": settings.PROJECT_NAME}
