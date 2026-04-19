import logging
from fastapi import FastAPI

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Face Swap API", version="1.0.0")


@app.get("/")
async def root():
    logger.info("GET / — root endpoint called")
    return "Face Swap API is running. Use POST /face-swap to swap faces."


@app.get("/health")
async def health_check():
    logger.info("GET /health — health check called")
    return {"status": "ok", "message": "Service is healthy"}
