from app.services.reasoning_service import build_reasoning_log

log = build_reasoning_log(
    email=None,
    category="Refund Request",
    sentiment="Negative",
    priority="High",
    rag_sources=[
        "refund_policy.md",
        "escalation_matrix.md"
    ]
)

print(log)