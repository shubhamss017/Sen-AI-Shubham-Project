from sqlalchemy import text
from app.db.database import engine

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version()"))
        print("Database Connected Successfully")
        print(result.fetchone())
except Exception as e:
    print("Connection Failed")
    print(e)
