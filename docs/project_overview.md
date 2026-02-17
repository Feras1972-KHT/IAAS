# IAAS Project Analysis & Refactoring Plan

## 1. Project Overview

**Intelligent Academic Advisory System (IAAS)** is a capstone software engineering project designed to provide automated academic advising to students.

- **Primary Features**:
  1. **Chat Advisor**: AI-powered (OpenAI GPT-4o-mini) chatbot for course recommendations.
  2. **Degree Progress**: Visual dashboard showing completed/remaining courses.
  3. **Admin Dashboard**: Dataset management (uploading CSVs) and system monitoring.

## 2. Current State Analysis

The repository currently contains **only documentation**:

- `SE495_Design_Document.pdf` (Architecture, Class Design, Deployment)
- `SRSV2 (1).pdf` (Functional/Non-Functional Requirements)
- `End-of-Semester Progress Report (1) (1).pdf`
- `README.md`

**CRITICAL FINDING**: There is **no source code** in the repository. The "Refactoring" requested by the user effectively entails **initial project scaffolding** and implementation of the design architecture.

## 3. Architecture Design (from Docs)

Based on the Design Document, the system follows a **Layered Client-Server Architecture**:

### Tech Stack

- **Backend**: Python (FastAPI)
- **Database**: SQLite (local file)
- **Frontend**: Web-based (HTML/CSS/JS)
- **AI**: OpenAI API
- **Testing**: PyTest

### Logical Layers

1. **API Layer**: FastAPI Routers (`/api/chat`, `/api/progress`, `/admin/...`)
2. **Service Layer**: Business Logic (`AdvisorEngine`, `DegreeProgressService`, `DatasetValidator`)
3. **Repository Layer**: Data Access (`StudentRepository`, `CourseRepository`)
4. **Data Layer**: SQLite Database

## 4. Proposed Refactoring (Scaffolding) Plan

Since there is no code to clean up, I propose to **build the project skeletons** adhering to the design patterns specified in the documentation.

### Directory Structure

```
IAAS/
├── backend/
│   ├── app/
│   │   ├── api/            # Route controllers
│   │   ├── core/           # Config, Security, Logging
│   │   ├── models/         # Pydantic & SQLAlchemy models
│   │   ├── repositories/   # DB access
│   │   ├── services/       # Business logic (Advisor, Progress)
│   │   └── main.py         # Entry point
│   ├── tests/
│   └── requirements.txt
├── frontend/
│   ├── static/             # CSS, JS
│   └── templates/          # HTML
├── data/                   # SQLite db, sample CSVs
└── README.md               # Updated documentation
```

### Next Steps

1. Create the file structure above.
2. Initialize `requirements.txt` with dependencies (`fastapi`, `uvicorn`, `sqlalchemy`, `openai`, `pydantic`).
3. Create a basic `main.py` application entry point.
4. Create empty service/repository classes as placeholders based on the Design Doc.
5. Create a `README.md` with setup instructions.
