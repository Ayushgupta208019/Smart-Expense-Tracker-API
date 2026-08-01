from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()

expense_data = []

class Expense(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    date: date


@app.post("/expense")
def add_expense(expense: Expense):
    expense_data.append(expense)
    return {
        "message": "Expense added successfully",
        "data": expense
    }

@app.get("/expenses")
def get_expenses():
    return {
        "message": "Expenses retrieved successfully",
        "data": expense_data
    }

