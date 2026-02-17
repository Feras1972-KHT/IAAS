# Intelligent Academic Advisory System (IAAS)

> **Note**: This project structure has been scaffolded based on the design documentation.

## Overview

The Intelligent Academic Advisory System (IAAS) is a software system designed to support university students in academic decision-making. It assists with course planning, degree progress tracking, and advisory recommendations based on predefined rules and structured academic data.

## Features

- **Chat Advisor**: AI-powered course recommendations using OpenAI GPT-4o-mini.
- **Degree Progress**: Visual dashboard for tracking academic progress.
- **Admin Tools**: Dataset management and system monitoring.

## Tech Stack

- **Backend**: Python 3.9+ (FastAPI)
- **Database**: SQLite
- **Frontend**: HTML/CSS/JS (Templates)
- **AI**: OpenAI API

## Project Structure

```
IAAS/
├── backend/
│   ├── app/
│   │   ├── api/            # Route controllers
│   │   ├── core/           # Config, Security
│   │   ├── services/       # Business logic (Advisor, Progress)
│   │   └── main.py         # Entry point
│   ├── tests/
│   └── requirements.txt
├── frontend/
│   ├── static/             # CSS, JS
│   └── templates/          # HTML
├── data/                   # SQLite db, sample CSVs
└── README.md
```

## Setup Instructions

### Prerequisites

- Python 3.9+
- OpenAI API Key

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Feras1972-KHT/IAAS.git
   cd IAAS
   ```

2. **Backend Setup**

   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Environment Configuration**
   Create a `.env` file in `backend/` with your API key:

   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

4. **Run the Server**
   ```bash
   # From the backend directory
   python -m app.main
   ```
   The API will be available at `http://localhost:8000`.
   API Documentation: `http://localhost:8000/docs`.

## Documentation

- `SE495_Design_Document.pdf`: System Architecture and Design.
- `SRSV2 (1).pdf`: Software Requirements Specification.
