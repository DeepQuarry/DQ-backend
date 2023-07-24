from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.api import main_router
from app.core.config import settings
from app.core.log import generate_logger

logger = generate_logger()
logger.info("Starting API")

# origins = [
#     "*"  # just for now
#     # "https://deepquarry-pi.vercel.app",
#     # "https://deepquarry.vercel.app" "http://localhost",
#     # "http://localhost:8080",
# ]
#
# regex_origin = ["https?//.*\.deepquarry.*vercel.app", "https?//.*\.localhost:?\d*"]

# middleware = [
#     CORSMiddleware,
#     allow_origins=["*"],
#     # allow_origin_regex=regex_origin,
#     allow_credentials=True,
#     allow_methods=["GET", "POST"],
#     allow_headers=["*"],
# ]


middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        # # allow_origin_regex=regex_origin,
        # allow_credentials=True,
        # allow_methods=["GET", "POST"],
        # allow_headers=["*"],
    )
]

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json", middleware=middleware
)


app.include_router(main_router, prefix=settings.API_V1_STR)


@app.get("/")
async def main():
    return {"message": settings.PROJECT_NAME}
