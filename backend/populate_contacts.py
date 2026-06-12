from app.db.database import SessionLocal
from app.models.email import Email
from app.models.contact import Contact

db = SessionLocal()

emails = db.query(Email).all()

unique_emails = set()

for email in emails:
    unique_emails.add(email.sender)

for email_address in unique_emails:

    existing = (
        db.query(Contact)
        .filter(Contact.email == email_address)
        .first()
    )

    if existing:
        continue

    contact = Contact(
        email=email_address,
        name=email_address.split("@")[0],
        account_type="Unknown",
        status="Active",
        annual_value="0"
    )

    db.add(contact)

db.commit()

print(f"Created {len(unique_emails)} contacts")