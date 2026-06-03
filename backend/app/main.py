from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core import config
from app.api import admin, chat, pages
from app.db.base import Base
from app.db.session import engine
from app.models import Course, Student  

# create tables on startup if they don't exist
Base.metadata.create_all(bind=engine)


app = FastAPI(title=config.settings.PROJECT_NAME)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# JSON health check (moved off / so the chat page can live at root)
@app.get("/api/health")
def health():
    return {"message": "Welcome to IAAS API", "status": "running"}


# connect the routers
app.include_router(pages.router, tags=["pages"])
app.include_router(chat.router, prefix=config.settings.API_V1_STR + "/chat", tags=["chat"])
app.include_router(admin.router, prefix=config.settings.API_V1_STR + "/admin", tags=["admin"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
