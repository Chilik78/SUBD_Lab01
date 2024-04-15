from fastapi import FastAPI
from server.routers.routers import *
import uvicorn

app = FastAPI()
app.include_router(crew_route)
app.include_router(tech_route)

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)