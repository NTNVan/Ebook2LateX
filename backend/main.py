from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Chao mung ban den voi Ebook2LateX!"}
@app.get("/multiply/{number}")
def multiply_number(number: int):
    result = number * 10
    return {"input": number, "result": result}
@app.get("/buy-shoes")
def buy_shoes(brand: str, size: int):
    return {
        "message": f"Bạn muốn mua giày {brand} kích thước {size} đúng không?"
    }