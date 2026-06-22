
def format_logs(logs: list[dict]) -> str:
    """Prepare logs before sending them to the model.

    TODO (Step 7 - Analyze Incident with Gemini)
    TODO (Task 2 - Log Context)
    """
    raise NotImplementedError("Implement Task 2")


def build_prompt(log_text: str) -> str:
    """Build the prompt for Gemini.

    TODO (Task 3 - Prompt Design)
    """
    raise NotImplementedError("Implement Task 3")


def analyze_incident(logs: list[dict]):
    """Call Gemini and return the analysis result.

    TODO (Step 7 - Analyze Incident with Gemini)
    TODO (Task 4 - Confidence Score)
    """
    raise NotImplementedError("Implement Step 7 / Task 4")
