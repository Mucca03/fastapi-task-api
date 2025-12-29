from datetime import datetime
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

class TaskOut(TaskBase):
    id: int
    completed: bool
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
