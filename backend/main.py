from fastapi import FastAPI

app = FastAPI(
    title="CitizenPath API",
    description="AI-powered government portal task verification",
    version="0.1.0"
)


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
