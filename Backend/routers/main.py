from fastapi import APIRouter

router = APIRouter(
    tags = ["Main"]
)

@router.get("/")
def main():
    return {"description": "this is main page"}