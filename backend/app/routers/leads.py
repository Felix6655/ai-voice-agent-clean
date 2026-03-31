from datetime import datetime, timezone

from fastapi import APIRouter

from app.schemas.lead import LeadCreate

router = APIRouter(tags=["leads"])

LEADS_DB = []


@router.get("/leads")
async def list_leads():
    return {
        "ok": True,
        "count": len(LEADS_DB),
        "items": LEADS_DB,
    }


@router.post("/leads")
async def create_lead(payload: LeadCreate):
    lead = payload.model_dump()
    lead["submitted_at"] = datetime.now(timezone.utc).isoformat()
    LEADS_DB.append(lead)

    return {
        "service": lead["service"],
        "name": lead["name"],
        "phone": lead["phone"],
        "city": lead["city"],
        "state": lead["state"],
        "description": lead["description"],
        "submitted_at": lead["submitted_at"],
    }