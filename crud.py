from models import TestUser
from fastapi import HTTPException, status, Response
from fastapi.routing import APIRouter
from schema import TestUserBase

router = APIRouter(tags=['TestUser'])

@router.post("/create_user")
async def create_user(user_data: TestUserBase):
    try:
        user = await TestUser.create(**user_data.model_dump())
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

@router.get("/read_user")
async def read_user(username: str, password: str):
    try:
        user = await TestUser.get(username=username, password=password)
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get("/get_all_users")
async def get_all_users():
    try:
        users = await TestUser.all()
        return users
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"An error occurred while fetching users: {str(e)}",
        )

