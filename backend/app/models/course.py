from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from app.db.base import Base


# association table for course prerequisites
course_prerequisites = Table(
    "course_prerequisites",
    Base.metadata,
    Column("course_id", ForeignKey("courses.id"), primary_key=True),
    Column("prerequisite_id", ForeignKey("courses.id"), primary_key=True),
)


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    code = Column(String(20), unique=True, index=True, nullable=False)
    name = Column(String(200), nullable=False)
    credits = Column(Integer, nullable=False)
    description = Column(String(1000), nullable=True)
    semester = Column(Integer, nullable=True)

    # self-referential many-to-many
    prerequisites = relationship(
        "Course",
        secondary=course_prerequisites,
        primaryjoin=id == course_prerequisites.c.course_id,
        secondaryjoin=id == course_prerequisites.c.prerequisite_id,
    )

    def __repr__(self):
        return f"<Course {self.code}>"
