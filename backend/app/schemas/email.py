from pydantic import BaseModel
from datetime import datetime


class EmailCreate(BaseModel):
    message_id: str
    thread_id: str
    sender: str
    subject: str | None = None
    body: str | None = None
    timestamp: datetime