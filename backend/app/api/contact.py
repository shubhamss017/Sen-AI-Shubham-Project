from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.contact import Contact

router = APIRouter()


@router.get("/contact/{contact_id}")
def get_contact(
    contact_id: int,
    db: Session = Depends(get_db)
):
    contact = (
        db.query(Contact)
        .filter(Contact.id == contact_id)
        .first()
    )

    if not contact:
        raise HTTPException(
            status_code=404,
            detail="Contact not found"
        )

    return {
        "id": contact.id,
        "email": contact.email,
        "name": contact.name,
        "company": contact.company,
        "account_type": contact.account_type,
        "status": contact.status,
        "annual_value": contact.annual_value
    }