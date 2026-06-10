from elasticsearch import Elasticsearch

from app.config.confs import ELASTICSEARCH_INDEX, RETRIEVAL_SIZE, DETECTION_THRESHOLD
es = Elasticsearch(ELASTICSEARCH_URL)


def fetch_recent_errors(index: str = ELASTICSEARCH_INDEX, size: int = RETRIEVAL_SIZE) -> list[dict]:
    """Retrieve recent error logs from Elasticsearch.

    TODO (Step 5 - Retrieve Failure Logs)
    TODO (Task 2 - Log Context)
    """
    raise NotImplementedError("Implement Step 5 / Task 2")


def detect_failure_spike(logs: list[dict], threshold: int = DETECTION_THRESHOLD) -> bool:
    """Detect whether the current error volume should trigger analysis.

    TODO (Step 6 - Failure Spike Detection)
    TODO (Task 1 - Failure Detection)
    """
    raise NotImplementedError("Implement Step 6 / Task 1")
