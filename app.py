from fastapi import FastAPI
from fastapi.responses import JSONResponse
from air_quality.air_quality import get_air_quality

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Air Quality API"}


@app.get("/air_quality")
async def read_air_quality():
    data = get_air_quality()
    if data:
        return JSONResponse(content=data)
    else:
        return JSONResponse(content={"error": "Failed to read air quality data"}, status_code=500)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
