from pydantic import BaseModel, EmailStr
from typing import Optional

VALID_STATUS = ["applied", "interview", "selected", "rejected"]

class CandidateCreate(BaseModel):
    name: str
    email: EmailStr
    skill: str
    status: str

class CandidateResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    skill: str
    status: str

    class Config:
        from_attributes = True

class UpdateStatus(BaseModel):
    status: str