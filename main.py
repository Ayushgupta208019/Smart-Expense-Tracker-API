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
