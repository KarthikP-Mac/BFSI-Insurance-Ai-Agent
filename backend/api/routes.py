from fastapi import APIRouter
from backend.models.schemas import ChatRequest, ChatResponse
from backend.services.crag import run_crag_pipeline

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    result = await run_crag_pipeline(request.query, request.session_id)
    return ChatResponse(
        answer=result["answer"],
        confidence_level=result["confidence_level"],
        compliance_status=result["compliance_status"],
        sources=result["sources"],
        trace=result["trace"]
    )
