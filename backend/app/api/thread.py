from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.email import Email

router = APIRouter()


@router.get("/thread/{thread_id}")
def get_thread(
    thread_id: str,
    db: Session = Depends(get_db)
):

    emails = (
        db.query(Email)
        .filter(Email.thread_id == thread_id)
        .order_by(Email.timestamp)
        .all()
    )

    return emails