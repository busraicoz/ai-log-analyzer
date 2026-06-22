from elasticsearch import Elasticsearch

from app.config.confs import ELASTICSEARCH_URL

es = Elasticsearch(ELASTICSEARCH_URL)


def fetch_recent_errors(index="mortgage-logs-*", size=50):
    query = {
        "size": size,
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "message": "ERROR"
                        }
                    },
                    {
                        "range": {
                            "@timestamp": {
                                "gte": "now-15m"
                            }
                        }
                    }
                ]
            }
        },
        "sort": [
            {"@timestamp": {"order": "desc"}}
        ]
    }

    response = es.search(index=index, body=query)

    return [hit["_source"] for hit in response["hits"]["hits"]]


def detect_failure_spike(logs, threshold=5):
    if not logs:
        return False

    error_count = len(logs)

    return error_count >= threshold
