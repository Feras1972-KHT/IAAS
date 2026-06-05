# pages.py - serves the HTML pages for the chat UI and progress dashboard

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import Course, Student
from app.services.prereq import get_eligible_courses


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


# friendly semester names
SEMESTER_NAMES = {
    1: "Freshman Fall",
    2: "Freshman Spring",
    3: "Sophomore Fall",
    4: "Sophomore Spring",
    5: "Junior Fall",
    6: "Junior Spring",
    7: "Senior Fall (+ Summer Internship)",
    8: "Senior Spring",
}


@router.get("/", response_class=HTMLResponse)
def chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})


@router.get("/admin", response_class=HTMLResponse)
def admin_page(request: Request, db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    students = db.query(Student).all()

    # group courses by semester for the checkbox form
    by_semester = {}
    for c in courses:
        sem = c.semester or 0
        if sem not in by_semester:
            by_semester[sem] = []
        by_semester[sem].append(c)
    sorted_semesters = sorted(by_semester.items())

    return templates.TemplateResponse("admin.html", {
        "request": request,
        "courses": courses,
        "students": students,
        "by_semester": sorted_semesters,
        "semester_names": SEMESTER_NAMES,
    })


@router.get("/progress", response_class=HTMLResponse)
def progress_page(request: Request, student_id: int = 1, db: Session = Depends(get_db)):
    # find the student
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    all_students = db.query(Student).all()
    courses = db.query(Course).all()

    # compute eligible courses
    completed_codes = []
    for c in student.completed_courses:
        completed_codes.append(c.code)

    eligible = get_eligible_courses(student, courses)
    eligible_codes = []
    for c in eligible:
        eligible_codes.append(c.code)

    # group courses by semester with status
    by_semester = {}
    for course in courses:
        sem = course.semester or 0
        if sem not in by_semester:
            by_semester[sem] = []

        if course.code in completed_codes:
            status = "completed"
        elif course.code in eligible_codes:
            status = "eligible"
        else:
            status = "locked"

        by_semester[sem].append({
            "code": course.code,
            "name": course.name,
            "credits": course.credits,
            "status": status,
        })

    # sort semesters in order
    sorted_semesters = sorted(by_semester.items())

    # stats
    total_credits = 0
    for c in courses:
        total_credits += c.credits

    completed_credits = 0
    for c in student.completed_courses:
        completed_credits += c.credits

    percentage = 0
    if total_credits > 0:
        percentage = round(completed_credits / total_credits * 100)

    return templates.TemplateResponse("progress.html", {
        "request": request,
        "student": student,
        "all_students": all_students,
        "by_semester": sorted_semesters,
        "semester_names": SEMESTER_NAMES,
        "stats": {
            "completed_count": len(completed_codes),
            "total_count": len(courses),
            "completed_credits": completed_credits,
            "total_credits": total_credits,
            "percentage": percentage,
        },
    })
