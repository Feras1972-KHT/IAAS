# admin endpoints - add a single student via JSON

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import Course, Student


router = APIRouter()


class AddStudentRequest(BaseModel):
    name: str
    year: int
    major: str = "Software Engineering"
    completed_codes: list[str] = []


@router.post("/students")
def add_student(request: AddStudentRequest, db: Session = Depends(get_db)):
    # look up each completed course in the catalog
    completed_courses = []
    missing = []
    for code in request.completed_codes:
        course = db.query(Course).filter(Course.code == code).first()
        if course is None:
            missing.append(code)
        else:
            completed_courses.append(course)

    # if any code wasn't found, reject the whole request
    if missing:
        raise HTTPException(
            status_code=400,
            detail=f"Courses not found: {', '.join(missing)}"
        )

    # create the student and link completed courses
    student = Student(
        name=request.name,
        year=request.year,
        major=request.major,
    )
    for c in completed_courses:
        student.completed_courses.append(c)
    db.add(student)
    db.commit()

    return {"id": student.id, "name": student.name}
