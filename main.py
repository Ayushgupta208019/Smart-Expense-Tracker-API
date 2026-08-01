from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from fastapi import Query

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

@app.get("/expense/search")
def search_expense(title: str = Query(...)):
    filtered_expenses = [
        expense
        for expense in expense_data
        if title.lower() in expense.title.lower()
    ]

    return {
        "message": "Expenses retrieved successfully",
        "data": filtered_expenses
    }

@app.get("/expense/{expense_category}")
def get_expense(expense_category: str):
    filtered_expenses = [expense for expense in expense_data if expense.category.lower() == expense_category.lower()]
    if not filtered_expenses:
        return {
            "message": f"No expenses found for category: {expense_category}",
            "data": []
        }
    return {
        "message": "Expenses retrieved successfully",
        "data": filtered_expenses
    }

@app.delete("/expense/{expense_id}")
def delete_expense(expense_id: int):
    for expense in expense_data:
        if expense.id == expense_id:
            expense_data.remove(expense)
            return {
                "message": "Expense deleted successfully",
                "data": expense
            }
    return {
        "message": "Expense not found",
        "data": None
    }
from fastapi import Query







