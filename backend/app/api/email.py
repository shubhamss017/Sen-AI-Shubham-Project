from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.email import EmailCreate
from app.models.email import Email
from app.db.dependencies import get_db

router = APIRouter()


@router.post("/ingest")
def ingest_email(
    email: EmailCreate,
    db: Session = Depends(get_db)
):

    db_email = Email(
        message_id=email.message_id,
        thread_id=email.thread_id,
        sender=email.sender,
        subject=email.subject,
        body=email.body,
        timestamp=email.timestamp
    )

    db.add(db_email)
    db.commit()
    db.refresh(db_email)

    return {
        "message": "Email saved successfully",
        "id": db_email.id
    }