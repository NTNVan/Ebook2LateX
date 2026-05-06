from app.database import SessionLocal
from app.models import User, Document
from sqlalchemy import func

db = SessionLocal()

results = (
    db.query(User.full_name, func.count(Document.id))
    .join(Document, User.user_id == Document.user_id)
    .group_by(User.full_name)
    .all()
)

for name, count in results:
    print(f"{name}: {count} documents")

db.close()