from fastapi import APIRouter

from app.schemas.lead import LeadCreate
from app.routers.leads import create_lead

router = APIRouter(tags=["voice"])


@router.get("/voice/health")
async def voice_health():
    return {"ok": True, "service": "voice"}


@router.post("/voice/test")
async def voice_test(payload: LeadCreate):
    created = await create_lead(payload)
    return {
        "ok": True,
        "message": "Voice lead saved",
        "lead": created,
    }