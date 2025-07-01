from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("api/add")
def add_numbers(numbers: Numbers):
    return {"result": numbers.num1 + numbers.num2}