import json


def build_reasoning_log(
    email,
    category,
    sentiment,
    priority,
    rag_sources
):

    log = [
        {
            "step": 1,
            "thought": "Analyze customer email",
            "observation": f"Category={category}, Sentiment={sentiment}, Priority={priority}"
        }
    ]

    if rag_sources:

        log.append(
            {
                "step": 2,
                "thought": "Search knowledge base",
                "observation": f"Retrieved: {', '.join(rag_sources)}"
            }
        )

    if priority in ["High", "Critical"]:

        log.append(
            {
                "step": 3,
                "thought": "Check escalation necessity",
                "observation": "High priority issue detected"
            }
        )

    if sentiment == "Negative":

        log.append(
            {
                "step": 4,
                "thought": "Assess customer risk",
                "observation": "Negative sentiment increases churn risk"
            }
        )

    return json.dumps(log, indent=2)