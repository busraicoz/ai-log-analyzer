from vertexai.generative_models import GenerativeModel

from app.config.confs import GEMINI_MODEL

model = GenerativeModel(GEMINI_MODEL)


def format_logs(logs):
    return "\n".join(
        f"[{log.get('@timestamp')}] {log.get('serviceName')} - {log.get('message')}"
        for log in logs
    )

def build_prompt(log_text: str) -> str:
    """Build the prompt for Gemini.

    TODO (Task 3 - Prompt Design)
    """
    raise NotImplementedError("Implement Task 3")

def analyze_incident(logs):
    formatted_logs = format_logs(logs)

    prompt = f"""
    You are a Senior Site Reliability Engineer specializing in incident analysis.

    Analyze the following logs and return a JSON response with the following fields:
    - root_cause
    - explanation
    - severity (LOW, MEDIUM, HIGH, CRITICAL)
    - suggested_actions

    Logs:
    {formatted_logs}

    Respond ONLY with valid JSON. Do not include any additional text.
    """

    response = model.generate_content(prompt)

    return response.text
