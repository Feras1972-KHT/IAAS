# advisor service - calls OpenAI

import json

from openai import OpenAI

from app.core.config import settings
from app.models.schemas import ChatResponse, CourseRead
from app.services.prereq import get_eligible_courses


SYSTEM_PROMPT = (
    "You are an academic advisor for Software Engineering students at "
    "Alfaisal University. Recommend courses based on the student's "
    "completed courses and the eligible list provided. Only recommend "
    "from the eligible list."
)


class AdvisorEngine:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def get_recommendation(self, student, all_courses, query):
        # get eligible courses using the prereq engine
        eligible = get_eligible_courses(student, all_courses)

        # handle empty eligible list - no LLM call needed
        if not eligible:
            return ChatResponse(
                answer=f"{student.name} has no eligible courses remaining.",
                recommended_courses=[],
                source="rule-based",
            )

        # build the user prompt
        completed_codes = []
        for c in student.completed_courses:
            completed_codes.append(c.code)
        completed_codes.sort()

        eligible_lines = ""
        for c in eligible:
            eligible_lines += f"- {c.code}: {c.name} ({c.credits} cr)\n"

        user_msg = f"""Student: {student.name} (Year {student.year}, {student.major})
Completed courses ({len(completed_codes)}): {", ".join(completed_codes)}

Eligible courses for next semester (prerequisites met):
{eligible_lines}

Student question: {query}

Recommend 3-5 specific courses from the eligible list. Return JSON:
{{
  "answer": "2-4 sentence explanation",
  "recommended_codes": ["SE 310", "SE 324"]
}}"""

        # call OpenAI
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_msg},
            ],
            response_format={"type": "json_object"},
        )

        # parse the response
        parsed = json.loads(response.choices[0].message.content)
        recommended_codes = parsed.get("recommended_codes", [])

        # convert recommended codes to CourseRead objects
        # build a lookup dict so we can find courses by code quickly
        eligible_by_code = {}
        for c in eligible:
            eligible_by_code[c.code] = c

        recommended_courses = []
        for code in recommended_codes:
            if code in eligible_by_code:
                c = eligible_by_code[code]
                prereq_list = []
                for p in c.prerequisites:
                    prereq_list.append(p.code)
                recommended_courses.append(CourseRead(
                    id=c.id,
                    code=c.code,
                    name=c.name,
                    credits=c.credits,
                    description=c.description,
                    semester=c.semester,
                    prerequisites=prereq_list,
                ))

        return ChatResponse(
            answer=parsed.get("answer", ""),
            recommended_courses=recommended_courses,
            source="llm",
        )
