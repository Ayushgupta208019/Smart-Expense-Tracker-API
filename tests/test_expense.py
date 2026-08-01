from fastapi.testclient import TestClient
from src.main import app, expense_data

client = TestClient(app)


# Reset data before each test
def setup_function():
    expense_data.clear()


def test_add_expense():
    response = client.post(
        "/expense",
        json={
            "id": 1,
            "title": "Laptop Bag",
            "amount": 1499,
            "category": "Shopping",
            "date": "2026-08-06"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Expense added successfully"
    assert data["data"]["title"] == "Laptop Bag"
    assert data["data"]["amount"] == 1499


def test_get_all_expenses():
    client.post(
        "/expense",
        json={
            "id": 1,
            "title": "Shoes",
            "amount": 2500,
            "category": "Shopping",
            "date": "2026-08-06"
        }
    )

    response = client.get("/expenses")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Expenses retrieved successfully"
    assert len(data["data"]) == 1


def test_total_expenses():
    client.post(
        "/expense",
        json={
            "id": 1,
            "title": "Shoes",
            "amount": 2000,
            "category": "Shopping",
            "date": "2026-08-06"
        }
    )

    client.post(
        "/expense",
        json={
            "id": 2,
            "title": "Petrol",
            "amount": 1500,
            "category": "Transport",
            "date": "2026-08-07"
        }
    )

    response = client.get("/expense/total")

    assert response.status_code == 200
    assert response.json()["total_expenses"] == 3500


def test_total_expenses_by_category():
    client.post(
        "/expense",
        json={
            "id": 1,
            "title": "Mouse",
            "amount": 800,
            "category": "Shopping",
            "date": "2026-08-06"
        }
    )

    client.post(
        "/expense",
        json={
            "id": 2,
            "title": "Keyboard",
            "amount": 1200,
            "category": "Shopping",
            "date": "2026-08-07"
        }
    )

    response = client.get("/expense/total/Shopping")

    assert response.status_code == 200
    assert response.json()["total_expenses"] == 2000


def test_search_expense():
    client.post(
        "/expense",
        json={
            "id": 1,
            "title": "Laptop Bag",
            "amount": 1500,
            "category": "Shopping",
            "date": "2026-08-06"
        }
    )

    response = client.get("/expense/search?title=laptop")

    assert response.status_code == 200

    data = response.json()["data"]

    assert len(data) == 1
    assert data[0]["title"] == "Laptop Bag"


def test_get_expense_by_category():
    client.post(
        "/expense",
        json={
            "id": 1,
            "title": "Shoes",
            "amount": 2500,
            "category": "Shopping",
            "date": "2026-08-06"
        }
    )

    response = client.get("/expense/Shopping")

    assert response.status_code == 200

    data = response.json()["data"]

    assert len(data) == 1
    assert data[0]["category"] == "Shopping"


def test_get_invalid_category():
    response = client.get("/expense/Food")

    assert response.status_code == 200
    assert response.json()["data"] == []


def test_delete_expense():
    client.post(
        "/expense",
        json={
            "id": 1,
            "title": "Shoes",
            "amount": 2500,
            "category": "Shopping",
            "date": "2026-08-06"
        }
    )

    response = client.delete("/expense/1")

    assert response.status_code == 200
    assert response.json()["message"] == "Expense deleted successfully"

    response = client.get("/expenses")

    assert len(response.json()["data"]) == 0


def test_delete_invalid_expense():
    response = client.delete("/expense/100")

    assert response.status_code == 200
    assert response.json()["message"] == "Expense not found"