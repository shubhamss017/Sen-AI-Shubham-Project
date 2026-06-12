from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.email import Email
from app.models.action import Action

from app.rag.retriever import retrieve_context
from app.services.reasoning_service import build_reasoning_log
from app.services.gemini_service import analyze_email

router = APIRouter()


@router.post("/agent/execute/{email_id}")
def execute_agent(
    email_id: int,
    db: Session = Depends(get_db)
):

    email = (
        db.query(Email)
        .filter(Email.id == email_id)
        .first()
    )

    if not email:
        return {
            "error_code": "EMAIL_NOT_FOUND",
            "message": "Email not found"
        }

    # AI Analysis
    result = analyze_email(email.body)

    confidence = float(
        result.get("confidence", 0.0)
    )

    requires_human = (
        result.get("requires_escalation", False)
        or confidence < 0.70
    )

    # RAG Retrieval
    rag_context = retrieve_context(
        email.subject or email.body
    )

    # Reasoning Log
    reasoning_log = build_reasoning_log(
        email=email,
        category=result.get("category"),
        sentiment=result.get("sentiment"),
        priority=result.get("priority"),
        rag_sources=["knowledge_base"]
    )

    action_type = (
        "Escalate"
        if requires_human
        else "Auto-Reply"
    )

    action = Action(
        email_id=email.id,
        agent_reasoning_log=reasoning_log,
        action_type=action_type,
        confidence=str(confidence),
        proposed_content=result.get("suggested_reply"),
        escalation_reason=(
            "Low confidence or escalation requested"
            if requires_human
            else None
        )
    )

    db.add(action)
    db.commit()
    db.refresh(action)

    return {
        "email_id": email.id,
        "action_id": action.id,
        "category": result.get("category"),
        "sentiment": result.get("sentiment"),
        "priority": result.get("priority"),
        "confidence": confidence,
        "requires_human": requires_human,
        "action_type": action_type,
        "summary": result.get("summary"),
        "suggested_reply": result.get("suggested_reply")
    }