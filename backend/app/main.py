from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core import config
from app.api import admin, chat

app = FastAPI(title=config.settings.PROJECT_NAME)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to IAAS API", "status": "running"}

# TODO: Add routers here once created
# app.include_router(chat.router, prefix=config.settings.API_V1_STR + "/chat", tags=["chat"])
# app.include_router(admin.router, prefix=config.settings.API_V1_STR + "/admin", tags=["admin"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
