import pytest
from app import db, create_app


@pytest.fixture
def client():
    app = create_app({
        "SQLALCHEMY_DATABASE_URI": "postgresql://jnr@localhost:5432/taskdb_test",
        "TESTING": True,

    })

    with app.app_context():
        db.create_all()

    yield app.test_client()

    with app.app_context():
        db.drop_all()

def test_create_task(client):
    response = client.post("/tasks", json={"title": "Test Task"})
    assert response.status_code == 201

    result = response.get_json()
    assert result["title"] == "Test Task"

def test_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200

