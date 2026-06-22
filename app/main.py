from fastapi import FastAPI

app = FastAPI(title="AI Log Analyzer")
from app.service.incident_service import analyze_incident_flow


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze")
def analyze():
    return analyze_incident_flow()
