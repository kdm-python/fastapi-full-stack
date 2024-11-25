from fastapi import APIRouter


router = APIRouter()

@router.get("/", response_model=dict)
def welcome():
    return {"message": "dominance established over source code"}
