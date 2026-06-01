from fastapi import APIRouter

router = APIRouter()


# placeholder - admin dashboard comes later
@router.get("/")
def admin_root():
    return {"message": "admin endpoint - coming soon"}
