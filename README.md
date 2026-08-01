# Expense Tracker API

A simple REST API built with **FastAPI** for managing expenses.

## Features

* Add a new expense
* View all expenses
* Get expenses by category
* Search expenses by title
* Calculate total expenses
* Calculate total expenses by category
* Delete an expense
* Automated tests using `pytest`

---

## Project Structure

```text
your-repo/
│
├── README.md
├── AI_NOTES.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   └── main.py
└── tests/
    ├── __init__.py
    └── test_expense.py
```

---

## Prerequisites

* Python 3.10 or later

---

## Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## Start the Server

```bash
python -m uvicorn src.main:app --reload
```

The API will be available at:

* http://127.0.0.1:8000

Interactive API documentation:

* http://127.0.0.1:8000/docs

Alternative documentation:

* http://127.0.0.1:8000/redoc

---

## Run the Tests

```bash
python -m pytest
```

---

## API Endpoints

| Method | Endpoint                            | Description                       |
| ------ | ----------------------------------- | --------------------------------- |
| POST   | `/expense`                          | Add a new expense                 |
| GET    | `/expenses`                         | Get all expenses                  |
| GET    | `/expense/search?title=<title>`     | Search expenses by title          |
| GET    | `/expense/{expense_category}`       | Get expenses by category          |
| GET    | `/expense/total`                    | Get total expenses                |
| GET    | `/expense/total/{expense_category}` | Get total expenses for a category |
| DELETE | `/expense/{expense_id}`             | Delete an expense                 |

---

## Example Request

### Add Expense

```json
{
  "id": 1,
  "title": "Laptop Bag",
  "amount": 1499,
  "category": "Shopping",
  "date": "2026-08-06"
}
```
## Run the Tests

From the project root directory, run:

```bash
python -m pytest
```

If all tests pass, you should see output similar to:

```text
============================= test session starts =============================
collected 9 items

tests/test_expense.py .........                             [100%]

============================== 9 passed ==============================
```

To run a specific test file only:

```bash
python -m pytest tests/test_expense.py
```

