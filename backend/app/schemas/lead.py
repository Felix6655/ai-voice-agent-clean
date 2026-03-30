from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class LeadCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    phone: str = Field(..., min_length=3, max_length=30)
    service: str = Field(..., min_length=1, max_length=100)
    message: Optional[str] = Field(default=None, max_length=1000)
    urgency: str = Field(default="normal", max_length=20)


class Lead(BaseModel):
    id: int
    name: str
    phone: str
    service: str
    message: Optional[str] = None
    urgency: str
    status: str
    created_at: datetime
