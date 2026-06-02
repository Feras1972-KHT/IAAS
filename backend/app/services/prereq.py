# rule-based prerequisite validation

def get_eligible_courses(student, all_courses):
    #a course is eligible if all its prereqs are in the student's completed list
    #and the student hasn't already taken it
    completed_codes = {c.code for c in student.completed_courses}
    eligible = []
    for course in all_courses:
        if course.code in completed_codes:
            continue
        prereq_codes = {p.code for p in course.prerequisites}
        if prereq_codes.issubset(completed_codes):
            eligible.append(course)
    return eligible


def get_remaining_courses(student, all_courses):
    # everything the student hasn't completed yet
    completed_codes = {c.code for c in student.completed_courses}
    return [c for c in all_courses if c.code not in completed_codes]
