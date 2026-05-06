from faker import Faker
import uuid
from app.database import SessionLocal
from app.models import User

fake = Faker()
db = SessionLocal()

for _ in range(50):
    user = User(
        user_id=uuid.uuid4(),
        username_email=fake.email(),
        password_hash="123456",
        full_name=fake.name(),
        role="User"
    )
    db.add(user)

db.commit()
db.close()

print("Tạo 50 users xong!")