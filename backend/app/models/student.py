from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from app.db.base import Base


student_completed_courses = Table(
    "student_completed_courses",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True),
)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    year = Column(Integer, nullable=False)
    major = Column(String(100), nullable=False, default="Software Engineering")

    completed_courses = relationship(
        "Course",
        secondary=student_completed_courses,
    )

    def __repr__(self):
        return f"<Student {self.name}>"
