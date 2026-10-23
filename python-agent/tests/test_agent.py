from fastapi.testclient import TestClient
from app.main import app, answer_question

client = TestClient(app)

def test_health():
    assert client.get("/health").json()["status"] == "UP"

def test_reconciliation_guidance():
    result = answer_question("How do I reconcile a bank statement?")
    assert result.category == "Reconciliation"
    assert "transaction" in result.answer.lower()

def test_unknown_question_has_safe_fallback():
    result = answer_question("What should I do with this unusual issue?")
    assert result.category == "General finance operations"
    assert "confirm" in result.answer.lower()

def test_ask_endpoint_validates_question():
    response = client.post("/ask", json={"question": "reconcile"})
    assert response.status_code == 200
    assert response.json()["category"] == "Reconciliation"
