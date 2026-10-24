
from fastapi import APIRouter, HTTPException
from services.task_service import get_tasks, get_task

router = APIRouter(prefix="/api/tasks", tags=["tasks"])


@router.get("")
def list_tasks():
    return {"tasks": get_tasks()}


@router.get("/{task_id}")
def task_details(task_id: str):
    task = get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task
