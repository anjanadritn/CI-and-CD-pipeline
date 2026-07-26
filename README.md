# ci-cd-demo-app (Python / FastAPI)

Minimal FastAPI REST API — built specifically to learn CI/CD with Jenkins.

## Endpoints
- `GET /` → running message
- `GET /hello?name=Anjan` → greeting
- `GET /version` → version string
- `GET /health` → health check (for deployment verification later)

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run locally
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
Visit http://localhost:8000

## Run tests
```bash
pytest
```
