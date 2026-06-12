from fastapi import FastAPI
from app.api.email import router as email_router
from app.api.thread import router as thread_router
from app.api.contact import router as contact_router
from app.api.rag import router as rag_router
from app.api.analyze import router as analyze_router
from app.api.agent import router as agent_router
from app.api.agent_execute import router as agent_execute_router

app = FastAPI(
    title="SenAI CRM Intelligence Platform"
)

app.include_router(email_router, prefix="/api")
app.include_router(thread_router, prefix="/api")
app.include_router(contact_router, prefix="/api")
app.include_router(
    rag_router,
    prefix="/api"
)
app.include_router(
    analyze_router,
    prefix="/api"
)
app.include_router(
    agent_router,
    prefix="/api"
)
app.include_router(
    agent_execute_router,
    prefix="/api"
)

@app.get("/")
def health():
    return {"status": "running"}