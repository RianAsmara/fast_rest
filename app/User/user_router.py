from fastapi import APIRouter
from app.response import *
from .user_controller import UserController
from .user_schema import *

user_router = APIRouter()
controller = UserController()

@user_router.post("/user", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def add_user(res: Response, user: UserModel):
    return httpResponse(controller.post, res=res, user=user)

@user_router.get("/users", status_code=status.HTTP_200_OK, response_model=UsersResponse)
async def get_users(res: Response, limit: int = 10, page: int = 0):
    return httpResponse(controller.getUsers, res=res, limit=limit, page=page)