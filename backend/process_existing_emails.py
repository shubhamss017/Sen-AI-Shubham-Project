from app.db.database import SessionLocal
from app.models.email import Email
from app.services.gemini_service import analyze_email

db = SessionLocal()

emails = db.query(Email).all()

for email in emails:

    print(f"Processing {email.id}")

    result = analyze_email(email.body or "")

    email.category = result.get("category")
    email.sentiment = result.get("sentiment")
    email.priority = result.get("priority")
    email.requires_escalation = str(
        result.get("requires_escalation")
    )
    email.summary = result.get("summary")

db.commit()

print("All emails processed successfully")