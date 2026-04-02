from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas, crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Candidate Management API")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 1️⃣ Create Candidate
@app.post("/candidates", response_model=schemas.CandidateResponse)
def create_candidate(data: schemas.CandidateCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_candidate(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# 2️⃣ Get Candidates (with optional filter)
@app.get("/candidates", response_model=list[schemas.CandidateResponse])
def get_candidates(status: str = None, db: Session = Depends(get_db)):
    return crud.get_candidates(db, status)


# 3️⃣ Update Status
@app.put("/candidates/{candidate_id}/status", response_model=schemas.CandidateResponse)
def update_status(candidate_id: int, data: schemas.UpdateStatus, db: Session = Depends(get_db)):
    candidate = crud.update_candidate_status(db, candidate_id, data.status)

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    return candidate