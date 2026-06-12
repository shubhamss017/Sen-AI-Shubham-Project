from app.db.database import Base, engine
from app.models.email import Email
from app.models.contact import Contact
from app.models.action import Action

Base.metadata.create_all(bind=engine)

print("Tables Created Successfully") 