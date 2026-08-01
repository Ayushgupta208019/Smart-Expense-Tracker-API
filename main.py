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

@app.get("/expenses")
def get_expenses():
    return {
        "message": "Expenses retrieved successfully",
        "data": expense_data
    }

@app.get("/expense/total")
def total_expenses():
    total = sum(expense.amount for expense in expense_data)
    return {
        "message": "Total expenses calculated successfully",
        "total_expenses": total
    }

@app.get("/expense/total/{expense_category}")
def total_expenses_by_category(expense_category: str):
    total = sum(expense.amount for expense in expense_data if expense.category.lower() == expense_category.lower())
    return {
        "message": f"Total expenses for category '{expense_category}' calculated successfully",
        "total_expenses": total
    }

