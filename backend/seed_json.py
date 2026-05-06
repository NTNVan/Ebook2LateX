import json
import uuid
from app.database import SessionLocal
from app.models import FormulaEntry, Document, User

db = SessionLocal()

# 1. Tạo user
user = User(
    user_id=uuid.uuid4(),
    username_email="json_user@gmail.com",
    password_hash="123456"
)
db.add(user)
db.flush()

# 2. Tạo document
doc = Document(
    id=uuid.uuid4(),
    user_id=user.user_id,
    file_name="json_file.pdf",
    file_path_url="/uploads/json.pdf"
)
db.add(doc)
db.flush()

# 3. Đọc JSON
with open("data.json") as f:
    data = json.load(f)

# 4. Insert formula
for item in data:
    formula = FormulaEntry(
        id=uuid.uuid4(),
        document_id=doc.id,  # ✅ FIX CHỖ NÀY
        latex_content=item["latex"],
        order_index=1
    )
    db.add(formula)

db.commit()
db.close()

print("✅ Seed JSON thành công!")