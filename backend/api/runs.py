
from fastapi import APIRouter, HTTPException

from services.run_service import create_run, get_run, TaskNotFoundError
from schemas import StartRunRequest, RunResponse


router = APIRouter(
    prefix="/api/runs",
    tags=["Runs"]
)


@router.post("", response_model=RunResponse)
async def start_run(request: StartRunRequest):
    """
    Create a new run.
    """

    try:
        run = await create_run(request.task_id)
    except TaskNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return run


@router.get("/{run_id}", response_model=RunResponse)
async def get_run_status(run_id: str):
    """
    Retrieve an existing run.
    """

    run = await get_run(run_id)

    if run is None:
        raise HTTPException(
            status_code=404,
            detail="Run not found"
        )

    return run
