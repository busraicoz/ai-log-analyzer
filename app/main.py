from fastapi import FastAPI

app = FastAPI(title="AI Log Analyzer")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze")
def analyze():
    """Main workflow endpoint.
    TODO (Step 8 - Expose Incident Analysis API)
    TODO (Task 5 - API Response)
    """
    raise NotImplementedError("Implement Step 8 / Task 5")