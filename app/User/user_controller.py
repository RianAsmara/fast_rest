from .user_model import UserModel
from .user_schema import UsersResponse, UserModel, UserResponse

class UserController:

    def create_user(self, user: UserModel) -> UserResponse:
        response = UserResponse()
        
        response.bad_request()
        added_user = UserModel.add_user(user)
        
        if added_user is None:
            response.message = "User already exists"
            return response

        response = UserResponse(data=added_user.to_model())
        response.created()

        return response

    
    def get_users(self, limit, page):
        response = UsersResponse()
        users = UserModel.get_users(limit, page)
        users = [u.to_model() for u in users]
        response.data = users
        response.meta.totals = len(users)
        response.meta.limit = limit
        response.meta.current_page = page
        response.meta.next_page = page + 1
        response.meta.previous_page = page - 1
        return response