from fastapi import FastAPI
import logging
from fastapi.responses import JSONResponse
from air_quality.air_quality import get_air_quality

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Air Quality API"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.get("/air_quality")
async def read_air_quality():
    try:
        data = get_air_quality()
        if not data:
            logger.warning("No air quality data available")
            return JSONResponse(content={"error": "No data"}, status_code=404)
        logger.info("Air quality data retrieved successfully")
        return JSONResponse(content=data)
    except Exception as e:
        logger.error(f"Error retrieving air quality data: {e}")
        return JSONResponse(content={"error": "Server error"}, status_code=500)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
