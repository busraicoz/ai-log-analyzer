from fastapi import FastAPI
from datetime import datetime

from app.service.log_service import fetch_recent_errors, detect_failure_spike
from app.service.ai_service import analyze_incident

app = FastAPI(title="AI Log Analyzer")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/analyze")
def analyze():
    """Main workflow endpoint.
    TODO (Step 8 - Expose Incident Analysis API)
    TODO (Task 5 - API Response)
    """

    logs = fetch_recent_errors()

    if not detect_failure_spike(logs):
        return {
            "status": "no_incident",
            "timestamp": datetime.utcnow().isoformat()
        }

    analysis = analyze_incident(logs)

    return {
        "status": "incident_detected",
        "analysis": analysis
    }