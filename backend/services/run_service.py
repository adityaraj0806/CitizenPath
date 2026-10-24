from uuid import uuid4
from typing import Optional

from schemas import RunResponse
from services.task_service import get_task


# Temporary in-memory storage (lost on restart)
RUNS: dict[str, RunResponse] = {}


class TaskNotFoundError(Exception):
    """Raised when a run is requested for a task_id that does not exist."""


async def create_run(task_id: str) -> RunResponse:
    """
    Create a new run for an existing task.

    The run is only queued. No execution has happened, so there is no
    result, score, evidence, or verification yet. The runner (not yet
    implemented) is responsible for updating the run later.
    """

    if get_task(task_id) is None:
        raise TaskNotFoundError(task_id)

    run = RunResponse(run_id=str(uuid4()), task_id=task_id)

    RUNS[run.run_id] = run

    return run


async def get_run(run_id: str) -> Optional[RunResponse]:
    """
    Retrieve a run by its ID.
    """

    return RUNS.get(run_id)
