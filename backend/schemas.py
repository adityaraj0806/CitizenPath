
from pydantic import BaseModel, Field
from typing import Any, Literal, Optional


RunStatus = Literal["queued", "running", "completed", "blocked", "failed"]


class Task(BaseModel):
    id: str
    title: str
    description: str
    start_url: str
    instructions: list[str]


class StartRunRequest(BaseModel):
    task_id: str


class Verification(BaseModel):
    verified: bool = False
    checks: list[Any] = Field(default_factory=list)


class Evidence(BaseModel):
    source_urls: list[str] = Field(default_factory=list)


class RunResponse(BaseModel):
    run_id: str
    task_id: str
    status: RunStatus = "queued"

    score: Optional[float] = None
    summary: Optional[str] = None

    result: Optional[dict[str, Any]] = None

    verification: Verification = Field(
        default_factory=Verification
    )

    evidence: Evidence = Field(
        default_factory=Evidence
    )

    blocker: Optional[str] = None
    blockers: list[str] = Field(default_factory=list)

    progress: int = 0
    current_step: str = "Queued"

    error: Optional[str] = None
