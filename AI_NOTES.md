# AI_NOTES.md

## AI Tools Used

I used ChatGPT during development to understand FastAPI concepts, debug issues, and improve parts of my implementation. The overall project structure, endpoint implementation, and integration were completed by me, while ChatGPT was used as a learning and troubleshooting assistant.

## 1. Which parts were AI-generated vs. written by me

### Written by me

* Overall Expense Tracker API implementation.
* CRUD endpoints and API flow.
* In-memory storage using a Python list.
* Project structure and endpoint integration.
* Testing the APIs using FastAPI Swagger UI.

### Where I used ChatGPT

* Helped identify why filtering by category was not working. After adding the filter route, it was returning empty results because of the route order and routing conflict. ChatGPT explained the issue and how to fix it.
* Suggested making category comparison case-insensitive using:

  ```python
  expense.category.lower() == expense_category.lower()
  ```
* Suggested using the `date` type from `datetime` instead of storing dates as plain strings.
* Explained the purpose of `BaseModel` and `Query(...)` in FastAPI.
* Helped me understand how to organize the project using the required `src/` and `tests/` folders.
* Helped me write the pytest test suite because I had not written FastAPI tests before.
* Helped prepare the `README.md` with the required installation, server, and test commands.

## 2. What I validated, tested, or changed

* I tested every endpoint manually using the FastAPI Swagger UI (`/docs`).
* I verified that expenses could be added, listed, searched, deleted, and that total expense calculations worked correctly.
* After ChatGPT suggested using case-insensitive comparisons, I tested searches using different capitalizations such as `Shopping`, `shopping`, and `SHOPPING`.
* I changed the `date` field from `str` to `datetime.date` after understanding that it provides automatic validation and enforces a consistent date format.
* I reviewed and ran the generated test cases, making sure they matched my API routes and responses.

## 3. AI suggestions I decided not to use

* ChatGPT suggested using a database (such as SQLite or PostgreSQL) instead of storing data in a Python list. I decided not to implement this because the assignment requirements could be completed using in-memory storage, and adding a database would have increased the complexity unnecessarily.
* ChatGPT also suggested restructuring the API into multiple modules (such as separate routers, services, and models). Since this is a small project, I kept the implementation in a single `main.py` file to keep it simple and easier to review.
* Some suggested improvements, such as advanced validation and custom exception handlers, were not included because they were outside the scope of this assignment.
