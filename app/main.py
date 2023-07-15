from core.log import generate_logger
from fastapi import FastAPI

logger = generate_logger()
logger.info("Starting API")

app = FastAPI()

origins = ["*"]

# add routers and middleware here


@app.get("/")
async def root():
    return {"message": "wsg"}
