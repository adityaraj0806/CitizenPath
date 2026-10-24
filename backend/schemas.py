from typing import Optional
from pydantic import BaseModel


class RunRequest(BaseModel):
    task_id: str


class RunResponse(BaseModel):
    run_id: str
    task_id: str
    status: str


class RunResult(BaseModel):
    run_id: str
    task_id: str
    status: str
    agent_claimed: bool = False
    final_url: Optional[str] = None
    evidence_text: Optional[str] = None
    blocker_type: Optional[str] = None
    steps: int = 0
    verified: bool = False
    score: Optional[float] = None
    error: Optional[str] = None
