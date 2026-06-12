import json
from datetime import datetime

from app.db.database import SessionLocal
from app.models.email import Email

db = SessionLocal()

with open("D:\sen ai 2\data\email-data-advanced.json", "r", encoding="utf-8") as f:
    emails = json.load(f)

for email in emails:

    existing = (
        db.query(Email)
        .filter(Email.message_id == email["message_id"])
        .first()
    )

    if existing:
        continue

    db_email = Email(
        message_id=email["message_id"],
        thread_id=email["thread_id"],
        sender=email["sender"],
        subject=email.get("subject"),
        body=email.get("body"),
        timestamp=datetime.fromisoformat(email["timestamp"])
    )

    db.add(db_email)

db.commit()

print("Dataset Loaded Successfully")