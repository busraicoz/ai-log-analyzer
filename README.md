# AI Log Analyzer

Base repo for the AI Workshop.

The project is intentionally incomplete. Core functionality will be implemented during the workshop.

## Setup

pip install -r requirements.txt
cp .env.example .env

## Run locally

uvicorn app.main:app --reload

## Run with Docker

Docker build and run:

    docker-compose up --build

## Guide mapping
- Step 4 — Configure Environment → `app/config/confs.py`
- Step 5 — Retrieve Failure Logs → `app/service/log_service.py`
- Step 6 — Failure Spike Detection → `app/service/log_service.py`
- Step 7 — Analyze Incident with Gemini → `app/service/ai_service.py`
- Step 8 — Expose Incident Analysis API → `app/incident_service.py`
- Step 8 — Expose Incident Analysis API → `app/main.py`

## Tasks
- Task 1 — Failure Detection
- Task 2 — Log Context
- Task 3 — Prompt Design
- Task 4 — Confidence Score
- Task 5 — API Response


## Notes
Functions include TODO markers aligned with workshop tasks.