from dotenv import load_dotenv
import os

load_dotenv()

GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
GCP_LOCATION = os.getenv("GCP_LOCATION", "europe-west4")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-pro")
ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")
ELASTICSEARCH_INDEX = os.getenv("ELASTICSEARCH_INDEX", "logs-*")
DETECTION_THRESHOLD = int(os.getenv("DETECTION_THRESHOLD", "10"))
RETRIEVAL_SIZE = int(os.getenv("RETRIEVAL_SIZE", "50"))

def validate_config() -> None:
    required = {
        "GCP_PROJECT_ID": GCP_PROJECT_ID,
        "ELASTICSEARCH_URL": ELASTICSEARCH_URL,
    }
    missing = [key for key, value in required.items() if not value]
    if missing:
        raise ValueError(f"Missing required configuration: {', '.join(missing)}")
