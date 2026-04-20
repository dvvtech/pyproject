import logging
from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

rg_data: str = ""


@asynccontextmanager
async def lifespan(app: FastAPI):
    global rg_data
    file_path = Path(__file__).parent / "data" / "rg.txt"
    rg_data = file_path.read_text(encoding="utf-8")
    logger.info("rg.txt loaded (%d chars)", len(rg_data))
    yield


app = FastAPI(title="Face Swap API", version="1.0.0", lifespan=lifespan)


@app.get("/")
async def root():
    logger.info("GET / — root endpoint called")
    return "Face Swap API is running. Use POST /face-swap to swap faces."


@app.get("/health")
async def health_check():
    logger.info("GET /health — health check called")
    return {"status": "ok", "message": "Service is healthy"}
