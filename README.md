# Financial Data Insights and AI Agent Platform

A local-first portfolio demo of a serverless-style financial insights assistant. The Python service exposes a query endpoint and rule-based accounting guidance with an optional pluggable LLM adapter point; the Node.js service models a compact API Gateway/DynamoDB-style event store. The React UI provides a polished finance operations console.

## Requirements
- Python 3.10+
- Node.js 20+
- npm

## Start locally
Terminal 1:
```bash
cd python-agent
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
Terminal 2:
```bash
cd node-api
npm install
npm start
```
Terminal 3:
```bash
cd frontend
npm install
npm run dev
```
UI: `http://localhost:5173`; Python API: `http://localhost:8000`; Node API: `http://localhost:3001`.

## Demo endpoints
- Python `POST /ask` with `{"question":"How do I reconcile a bank fee?"}`
- Python `GET /health`
- Node `GET /api/insights`
- Node `POST /api/events`

## Architecture notes
AWS Lambda, API Gateway, DynamoDB, CloudWatch, CodeDeploy, SAML 2.0, and OpenID Connect are represented as integration seams and deployment guidance, not live AWS integrations. No credentials are included. Example impact numbers in the project brief are illustrative claims and are not measured by this repository.
