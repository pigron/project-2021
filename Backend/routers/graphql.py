from fastapi import APIRouter


router = APIRouter(
    tags = ["Graphql"]
)

@router.get("/graphql")
def main():
    return {"description": "graphql test page"}