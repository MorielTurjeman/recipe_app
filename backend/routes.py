from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def root():
    return {"message": "Server is up and running"}
