from sqlalchemy.orm import Session
from models import Candidate
from schemas import VALID_STATUS

def create_candidate(db: Session, data):
    if data.status not in VALID_STATUS:
        raise ValueError("Invalid status")

    candidate = Candidate(**data.dict())
    db.add(candidate)
    db.commit()
    db.refresh(candidate)
    return candidate


def get_candidates(db: Session, status=None):
    query = db.query(Candidate)
    if status:
        query = query.filter(Candidate.status == status)
    return query.all()


def update_candidate_status(db: Session, candidate_id: int, status: str):
    if status not in VALID_STATUS:
        raise ValueError("Invalid status")

    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()

    if not candidate:
        return None

    candidate.status = status
    db.commit()
    db.refresh(candidate)
    return candidate