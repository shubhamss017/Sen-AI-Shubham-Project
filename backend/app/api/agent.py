from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.email import Email
from app.models.contact import Contact

router = APIRouter()


@router.get("/agent/email/{email_id}")
def agent_email_analysis(
    email_id: int,
    db: Session = Depends(get_db)
):

    email = (
        db.query(Email)
        .filter(Email.id == email_id)
        .first()
    )

    if not email:
        return {"error": "Email not found"}

    contact = (
        db.query(Contact)
        .filter(Contact.email == email.sender)
        .first()
    )

    thread = (
        db.query(Email)
        .filter(
            Email.thread_id == email.thread_id
        )
        .order_by(Email.timestamp)
        .all()
    )

    thread_text = "\n".join([
        f"{e.sender}: {e.body}"
        for e in thread
    ])

    return {
        "email": {
            "id": email.id,
            "subject": email.subject,
            "category": email.category,
            "sentiment": email.sentiment,
            "priority": email.priority
        },
        "customer": {
            "email": contact.email if contact else None,
            "account_type": contact.account_type if contact else None,
            "status": contact.status if contact else None
        },
        "thread_messages": len(thread),
        "thread_preview": thread_text[:1000]
    }