from fastapi import FastAPI

from api.tasks import router as tasks_router
from api.runs import router as runs_router

app = FastAPI(
    title="CitizenPath API",
    description="AI-powered government portal task verification",
    version="0.1.0"
)

app.include_router(tasks_router)
app.include_router(runs_router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "citizenpath-backend"
    }


@app.get("/")
def home():
    return {
        "message": "CitizenPath backend is running"
    }
