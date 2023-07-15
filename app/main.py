from core.log import generate_logger
from fastapi import FastAPI

logger = generate_logger()
logger.info("Starting API")

app = FastAPI()

# add middleware, origins here


@app.get("/")
async def main():
    return {"message": "DeepQuarry API v1.0"}
