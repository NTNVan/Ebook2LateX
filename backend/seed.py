import uuid
from app.database import SessionLocal
from app.models import User, Document, FormulaEntry

def seed_data():
    db = SessionLocal()

    try:
        print("Đang tạo dữ liệu...")

        test_user = User(
            user_id=uuid.uuid4(),
            username_email="teo@dalat.edu.vn",
            password_hash="123456",
            full_name="Lê Văn Tèo",
            role="Admin"
        )
        db.add(test_user)
        db.flush()

        test_doc = Document(
            id=uuid.uuid4(),
            user_id=test_user.user_id,
            file_name="toan12.pdf",
            file_path_url="/uploads/toan12.pdf",
            status="Completed"
        )
        db.add(test_doc)
        db.flush()

        formula = FormulaEntry(
            id=uuid.uuid4(),
            document_id=test_doc.id,
            latex_content=r"\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
            order_index=1
        )
        db.add(formula)

        db.commit()
        print("✅ Thành công!")

    except Exception as e:
        print("❌ Lỗi:", e)
        db.rollback()

    finally:
        db.close()

if __name__ == "__main__":
    seed_data()