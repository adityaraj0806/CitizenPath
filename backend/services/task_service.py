
SAMPLE_TASKS = [
    {
        "id": "TASK-001",
        "title": "Find a government service",
        "description": "Locate a service on an official government portal",
        "start_url": "https://example.gov.in",
        "instructions": [
            "Open the official portal",
            "Locate the required service",
            "Identify the relevant information"
        ]
    }
]


def get_tasks():
    return SAMPLE_TASKS


def get_task(task_id: str):
    for task in SAMPLE_TASKS:
        if task["id"] == task_id:
            return task

    return None
