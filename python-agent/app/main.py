from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime, timezone

app = FastAPI(title="Financial Data Insights Agent", version="1.0.0")

class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=1000)

class AskResponse(BaseModel):
    answer: str
    category: str
    sources: list[str]
    generated_at: str
    mode: str = "local-demo"

PLAYBOOK = [
    (("reconcile", "matching", "bank statement"), "Reconciliation",
     "Compare normalized transaction date, amount, currency, and reference. Match exact candidates first, then route tolerances and unmatched items to a review queue.",
     ["Reconciliation playbook", "Journal control checklist"]),
    (("accrual", "accrued"), "Accrual accounting",
     "Record an expense and corresponding liability in the period the cost is incurred. Reverse or clear the accrual when the invoice is posted, following your organization's policy.",
     ["Month-end close checklist", "Accrual policy overview"]),
    (("variance", "budget", "forecast"), "Variance analysis",
     "Calculate actual minus budget, then separate price, volume, timing, and one-off effects. Prioritize material variances and attach an owner and explanation.",
     ["Variance analysis framework", "Management reporting guide"]),
    (("invoice", "vendor", "payable"), "Accounts payable",
     "Validate vendor, invoice number, currency, tax, duplicate risk, and purchase-order match before approval. Escalate exceptions rather than auto-approving them.",
     ["Invoice controls checklist", "Duplicate-payment controls"]),
]

def answer_question(question: str) -> AskResponse:
    normalized = question.lower()
    for terms, category, answer, sources in PLAYBOOK:
        if any(term in normalized for term in terms):
            return AskResponse(answer=answer, category=category, sources=sources,
                               generated_at=datetime.now(timezone.utc).isoformat())
    return AskResponse(
        answer=("I can help structure this accounting question. Identify the accounting period, source system, "
                "currency, relevant policy, and supporting evidence. For a posting or material judgment, confirm "
                "the answer with your finance controller before acting."),
        category="General finance operations",
        sources=["Finance operations knowledge base", "Internal policy review required"],
        generated_at=datetime.now(timezone.utc).isoformat()
    )

@app.get("/health")
def health():
    return {"status": "UP", "service": "financial-insights-agent"}

@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    return answer_question(request.question)
