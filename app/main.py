from fastapi import FastAPI, Request, Response
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


app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Salt to your taste
ALLOWED_ORIGINS = '*'    # or 'foo.com', etc.

# handle CORS preflight requests
@app.options('/{rest_of_path:path}')
async def preflight_handler(request: Request, rest_of_path: str) -> Response:
    response = Response()
    response.headers['Access-Control-Allow-Origin'] = ALLOWED_ORIGINS
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'
    return response

# set CORS headers
@app.middleware("http")
async def add_CORS_header(request: Request, call_next):
    response = await call_next(request)
    response.headers['Access-Control-Allow-Origin'] = ALLOWED_ORIGINS
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'
    return response

app.include_router(main_router, prefix=settings.API_V1_STR)


@app.get("/")
async def main():
    return {"message": settings.PROJECT_NAME}
