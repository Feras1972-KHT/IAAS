from app.db.base import Base
from app.db.session import engine, SeshLocal
from app.models import Course, Student


# Alfaisal University Software Engineering 4-year curriculum
# semester encoding: 1=Fr Fall, 2=Fr Spring, 3=So Fall, 4=So Spring,
# 5=Jr Fall, 6=Jr Spring, 7=Sr Fall (+summer internship), 8=Sr Spring
# tuple: (code, name, credits, semester, description, prereq_codes)
COURSES_DATA = [
    # --- Freshman Fall ---
    ("SE 100", "Programming for Engineers", 3, 1,
     "Introduction to programming for engineering students.", []),
    ("SE 100 L", "Programming for Engineers Lab", 1, 1,
     "Lab component for SE 100.", []),
    ("MAT 101", "Calculus I", 3, 1,
     "Limits, derivatives, integrals of single-variable functions.", []),
    ("PHU 103", "Physics I", 3, 1,
     "Classical mechanics, kinematics, dynamics.", []),
    ("PHU 103 L", "Physics I Lab", 1, 1,
     "Experimental physics lab for PHU 103.", []),
    ("ENG 101", "University Writing", 3, 1,
     "Academic writing skills.", []),
    ("COE 100", "Student Orientation & Academic Success", 1, 1,
     "Freshman orientation seminar.", []),
    # --- Freshman Spring ---
    ("SE 120", "Object-Oriented Programming I", 3, 2,
     "OOP fundamentals using Java or C++.", ["SE 100"]),
    ("SE 120 L", "OOP I Lab", 1, 2,
     "Lab component for SE 120.", ["SE 100"]),
    ("SE 151", "Discrete Mathematics", 3, 2,
     "Logic, sets, combinatorics, graph theory.", ["MAT 101"]),
    ("CHM 102", "General Chemistry", 3, 2,
     "Atomic structure, chemical bonding, reactions.", []),
    ("CHM 102 L", "General Chemistry Lab", 1, 2,
     "Lab component for CHM 102.", []),
    ("MAT 112", "Calculus II", 3, 2,
     "Sequences, series, multivariable calculus basics.", ["MAT 101"]),
    ("PHU 124", "Physics II", 3, 2,
     "Electromagnetism, waves, optics.", ["PHU 103"]),
    ("PHU 124 L", "Physics II Lab", 1, 2,
     "Lab component for PHU 124.", []),
    # --- Sophomore Fall ---
    ("SE 201", "Introduction to Software Engineering", 3, 3,
     "Software development lifecycle, methodologies, basic UML.", ["SE 120"]),
    ("SE 215", "Data Structures", 3, 3,
     "Arrays, linked lists, trees, hash tables, complexity.", ["SE 120"]),
    ("SE 215 L", "Data Structures Lab", 1, 3,
     "Lab component for SE 215.", ["SE 120"]),
    ("SE 220", "Object-Oriented Programming II", 3, 3,
     "Advanced OOP: design patterns, generics, exceptions.", ["SE 120"]),
    ("SE 220 L", "OOP II Lab", 1, 3,
     "Lab component for SE 220.", ["SE 120"]),
    ("SE 239", "Network Programming", 3, 3,
     "Socket programming, network protocols.", ["SE 120"]),
    ("MAT 212", "Linear Algebra", 3, 3,
     "Vectors, matrices, linear systems, eigenvalues.", ["MAT 112"]),
    # --- Sophomore Spring ---
    ("SE 225", "Software Requirements", 3, 4,
     "Requirements elicitation, analysis, specification.", ["SE 201"]),
    ("SE 252", "Database Management Systems", 3, 4,
     "Relational model, SQL, normalization.", ["SE 215"]),
    ("SE 252 L", "DBMS Lab", 1, 4,
     "Lab component for SE 252.", ["SE 215"]),
    ("CSE 250", "Introduction to Cybersecurity", 3, 4,
     "Security basics, threats, defenses, cryptography.", ["SE 215"]),
    ("EE 210", "Digital Logic Design", 3, 4,
     "Boolean algebra, combinational and sequential circuits.", ["MAT 112"]),
    ("EE 210 L", "Digital Logic Lab", 1, 4,
     "Lab component for EE 210.", []),
    ("ENG 222", "Technical Writing", 3, 4,
     "Writing technical documentation, reports.", ["ENG 101"]),
    # --- Junior Fall ---
    ("SE 301", "Analysis of Algorithms", 3, 5,
     "Algorithm design, complexity analysis, NP-completeness.", ["SE 215", "SE 151"]),
    ("SE 310", "Software Design and Architecture", 3, 5,
     "Architectural patterns, design principles.", ["SE 225"]),
    ("SE 314", "Operating Systems", 3, 5,
     "Processes, threads, memory management, file systems.", ["SE 215"]),
    ("SE 324", "Web Application Development", 3, 5,
     "Full-stack web development with modern frameworks.", ["SE 252"]),
    ("SE 324 L", "Web App Dev Lab", 1, 5,
     "Lab component for SE 324.", ["SE 252"]),
    ("STA 212", "Probability and Statistics", 3, 5,
     "Probability distributions, hypothesis testing, regression.", ["MAT 112"]),
    # --- Junior Spring ---
    ("SE 322", "Internet of Things Application Development", 3, 6,
     "IoT systems, sensors, edge computing.", ["SE 314"]),
    ("SE 328", "Mobile Application Development", 3, 6,
     "iOS and Android app development.", ["SE 324"]),
    ("SE 328 L", "Mobile App Dev Lab", 1, 6,
     "Lab component for SE 328.", ["SE 324"]),
    ("SE 354", "Software Project Management", 3, 6,
     "Project planning, scheduling, agile methodologies.", ["SE 310"]),
    ("MAT 224", "Numerical Methods", 3, 6,
     "Numerical algorithms for engineering problems.", ["MAT 212"]),
    # --- Junior Summer ---
    ("SE 390", "Software Engineering Internship", 0, 7,
     "Industry internship experience.", ["SE 310"]),
    # --- Senior Fall ---
    ("SE 412", "Software Testing and Quality Assurance", 3, 7,
     "Testing techniques, test-driven development, QA processes.", ["SE 310"]),
    ("SE 495", "Capstone Project I", 3, 7,
     "Capstone project planning, requirements, and design.", ["SE 310", "SE 354"]),
    # --- Senior Spring ---
    ("SE 423", "Software Construction and Processes", 3, 8,
     "Advanced software construction practices.", ["SE 310"]),
    ("SE 496", "Capstone Project II", 3, 8,
     "Capstone implementation, testing, and presentation.", ["SE 495"]),
    ("SE 481", "Ethics and Professional Development", 1, 8,
     "Engineering ethics, professional practice.", []),
]


# Alia is a 3rd year SE student, has completed all of freshman + sophomore
# plus a few junior fall courses
# this puts her around 58-60% degree progress, matching the SRS story
ALIA_COMPLETED = [
    # freshman fall
    "SE 100", "SE 100 L", "MAT 101", "PHU 103", "PHU 103 L", "ENG 101", "COE 100",
    # freshman spring
    "SE 120", "SE 120 L", "SE 151", "CHM 102", "CHM 102 L", "MAT 112",
    "PHU 124", "PHU 124 L",
    # sophomore fall
    "SE 201", "SE 215", "SE 215 L", "SE 220", "SE 220 L", "SE 239", "MAT 212",
    # sophomore spring
    "SE 225", "SE 252", "SE 252 L", "CSE 250", "EE 210", "EE 210 L", "ENG 222",
    # partial junior fall
    "SE 301", "SE 314", "STA 212",
]


# Faisal is a 4th year SE student in his final semester
# completed everything through senior fall, only 3 courses left to graduate
FAISAL_COMPLETED = [
    # freshman fall
    "SE 100", "SE 100 L", "MAT 101", "PHU 103", "PHU 103 L", "ENG 101", "COE 100",
    # freshman spring
    "SE 120", "SE 120 L", "SE 151", "CHM 102", "CHM 102 L", "MAT 112",
    "PHU 124", "PHU 124 L",
    # sophomore fall
    "SE 201", "SE 215", "SE 215 L", "SE 220", "SE 220 L", "SE 239", "MAT 212",
    # sophomore spring
    "SE 225", "SE 252", "SE 252 L", "CSE 250", "EE 210", "EE 210 L", "ENG 222",
    # junior fall (full)
    "SE 301", "SE 310", "SE 314", "SE 324", "SE 324 L", "STA 212",
    # junior spring (full)
    "SE 322", "SE 328", "SE 328 L", "SE 354", "MAT 224",
    # junior summer
    "SE 390",
    # senior fall
    "SE 412", "SE 495",
]


def seed():
    # start fresh every time we run the seed
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SeshLocal()

    # pass 1: create all courses first
    courses = {}
    for code, name, credits, semester, desc, _ in COURSES_DATA:
        c = Course(
            code=code,
            name=name,
            credits=credits,
            semester=semester,
            description=desc,
        )
        db.add(c)
        courses[code] = c
    db.commit()

    # pass 2: connect up the prereq relationships
    for code, _, _, _, _, prereq_codes in COURSES_DATA:
        course = courses[code]
        for pc in prereq_codes:
            course.prerequisites.append(courses[pc])
    db.commit()

    # add Alia
    alia = Student(
        name="Alia Al-Mansour",
        year=3,
        major="Software Engineering",
    )
    for code in ALIA_COMPLETED:
        alia.completed_courses.append(courses[code])
    db.add(alia)

    # add Faisal (4th year, almost graduating)
    faisal = Student(
        name="Faisal Alkahtani",
        year=4,
        major="Software Engineering",
    )
    for code in FAISAL_COMPLETED:
        faisal.completed_courses.append(courses[code])
    db.add(faisal)

    db.commit()

    print(f"Seeded {len(courses)} courses and 2 students.")
    print(f"Alia (year 3) has completed {len(ALIA_COMPLETED)} courses.")
    print(f"Faisal (year 4) has completed {len(FAISAL_COMPLETED)} courses.")
    db.close()


if __name__ == "__main__":
    seed()
