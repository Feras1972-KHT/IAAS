# chat endpoint - POST receives a query, returns advisor recommendation

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import Course, Student
from app.models.schemas import ChatRequest, ChatResponse
from app.services.advisor import AdvisorEngine


router = APIRouter()


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    # find the student
    student = db.query(Student).filter(Student.id == request.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # get all courses
    courses = db.query(Course).all()

    # run the advisor with conversation history
    advisor = AdvisorEngine()
    return advisor.get_recommendation(student, courses, request.query, request.history)
