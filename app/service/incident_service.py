import json
from app.service.log_service import fetch_recent_errors, detect_failure_spike
from app.service.ai_service import analyze_incident


def analyze_incident_flow():
    logs = fetch_recent_errors()

    if not detect_failure_spike(logs):
        return {
            "status": "NO_INCIDENT",
            "log_count": len(logs),
            "analysis": None
        }

    analysis_text = analyze_incident(logs)

    try:
        analysis = json.loads(analysis_text)
    except Exception:
        analysis = {
            "error": "Invalid AI output",
            "raw_output": analysis_text
        }

    return {
        "status": "INCIDENT_DETECTED",
        "log_count": len(logs),
        "analysis": analysis
    }