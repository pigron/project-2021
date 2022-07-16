from fastapi import APIRouter

router = APIRouter(
    tags = ["Login"]
)

@router.post("/login")
def login(id: str, password: str):
    return {"id": id, "password": password}