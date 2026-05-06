from app.database import SessionLocal
from app.models import FormulaEntry

db = SessionLocal()

keyword = "sqrt"

results = db.query(FormulaEntry).filter(
    FormulaEntry.latex_content.ilike(f"%{keyword}%")
).all()

for f in results:
    print(f.latex_content)

db.close()