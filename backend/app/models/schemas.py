from typing import Optional
from pydantic import BaseModel, ConfigDict


class CourseRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    code: str
    name: str
    credits: int
    description: Optional[str] = None
    semester: Optional[int] = None
    # prerequisites stored as list of course codes
    prerequisites: list[str] = []


class StudentRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    year: int
    major: str
    completed_courses: list[CourseRead] = []


class ChatRequest(BaseModel):
    student_id: int
    query: str
    history: list[dict] = []  # prior turns: [{role: user/assistant, content: text}]


class ChatResponse(BaseModel):
    answer: str
    recommended_courses: list[CourseRead] = []
    source: str  # llm or rule-based
