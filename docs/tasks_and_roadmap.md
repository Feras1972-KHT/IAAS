# IAAS Development Task Assignment & Roadmap

This document outlines the tasks required to develop the Intelligent Academic Advisory System (IAAS) based on the scaffolded project structure.

## 📅 Phase 1: Backend Foundation (Week 1)

**Goal:** Initialize the FastAPI server and database connection.

- [ ] **Task 1.1: Database Models** (`backend/app/models/params.py`)
  - Define SQLAlchemy models for `Student`, `Course`, `Prerequisite`, `Enrollment`.
  - Create Pydantic schemas for API requests/responses.
- [ ] **Task 1.2: Database Initialization** (`backend/app/db/init_db.py`)
  - Create a script to initialize the SQLite database tables.
  - Implement a seeding script to load sample CSV data (Students, Courses).
- [ ] **Task 1.3: API Enpoints Setup** (`backend/app/api/`)
  - Create basic CRUD routes for Students and Courses.
  - Verify data retrieval via Swagger UI (`/docs`).

## 🧠 Phase 2: Advisory Logic (Week 2)

**Goal:** Implement the core advisory intelligence (LLM + Rules).

- [ ] **Task 2.1: OpenAI Integration** (`backend/app/services/llm_service.py`)
  - Implement `AdvisorEngine` to call OpenAI API.
  - Construct prompt templates with student context (courses taken, remaining requirements).
- [ ] **Task 2.2: Rule-Based Fallback** (`backend/app/services/rules_service.py`)
  - Implement deterministic logic for course prerequisites.
  - Create the fallback mechanism when LLM is unavailable or quota exceeded.
- [ ] **Task 2.3: Degree Progress Logic** (`backend/app/services/progress_service.py`)
  - Algorithm to calculate completed credits vs. degree requirements.
  - Output JSON structure for frontend visualization.

## 💻 Phase 3: Frontend Development (Week 3)

**Goal:** Create the user interface for students and admins.

- [ ] **Task 3.1: Chat Interface** (`frontend/templates/chat.html`)
  - Design a simple chat UI (Student message input, Bot response area).
  - Connect to `/api/chat` endpoint using Fetch API / JavaScript.
- [ ] **Task 3.2: Progress Dashboard** (`frontend/templates/dashboard.html`)
  - Visualize degree progress (e.g., progress bars, checklist of courses).
  - Fetch data from `/api/progress`.
- [ ] **Task 3.3: Admin Panel** (`frontend/templates/admin.html`)
  - Interface for uploading CSV datasets.
  - View system logs and API usage stats.

## 🚀 Phase 4: Integration & Testing (Week 4)

**Goal:** Ensure system reliability and deployment readiness.

- [ ] **Task 4.1: Integration Testing**
  - Verify chat flows (Student asks -> LLM replies).
  - Verify fallback mechanism (Simulate OpenAI failure -> Rule-based reply).
- [ ] **Task 4.2: Documentation Update**
  - Update `README.md` with final deployment instructions.
  - Record demo walkthrough.
