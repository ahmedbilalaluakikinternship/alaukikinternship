from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Employee:
    name: str
    department: str
    employee_id: str = field(
        default_factory=lambda: str(uuid4())
    )


@dataclass
class Task:
    title: str
    assigned_to: Employee
    status: str = "Pending"
    task_id: str = field(
        default_factory=lambda: str(uuid4())
    )