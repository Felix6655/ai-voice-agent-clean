from datetime import datetime
from fastapi import APIRouter, HTTPException
from app.schemas.lead import LeadCreate, Lead

router = APIRouter(prefix="/api/leads", tags=["leads"])

LEADS_DB: list[Lead] = []
NEXT_ID = 1


@router.get("", response_model=list[Lead])
def list_leads() -> list[Lead]:
    return LEADS_DB


@router.get("/{lead_id}", response_model=Lead)
def get_lead(lead_id: int) -> Lead:
    for lead in LEADS_DB:
        if lead.id == lead_id:
            return lead
    raise HTTPException(status_code=404, detail="Lead not found")


@router.post("", response_model=Lead, status_code=201)
def create_lead(payload: LeadCreate) -> Lead:
    global NEXT_ID

    lead = Lead(
        id=NEXT_ID,
        name=payload.name,
        phone=payload.phone,
        service=payload.service,
        message=payload.message,
        urgency=payload.urgency,
        status="new",
        created_at=datetime.utcnow(),
    )

    LEADS_DB.append(lead)
    NEXT_ID += 1
    return lead
