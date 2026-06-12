from app.rag.retriever import retrieve_context
from app.services.gemini_service import analyze_email


def build_agent_prompt(
    email_body,
    thread_history,
    customer_profile,
    rag_context
):

    return f"""
You are an AI CRM Agent.

Customer Profile:
{customer_profile}

Conversation History:
{thread_history}

Knowledge Base:
{rag_context}

Latest Customer Email:
{email_body}

Tasks:
1. Determine customer intent
2. Recommend action
3. Decide if escalation is required
4. Draft a professional response

Return JSON:

{{
    "intent":"",
    "recommended_action":"",
    "escalate":true,
    "draft_reply":""
}}
"""