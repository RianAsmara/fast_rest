from app.User.user_router import user_router
from app import app

app.include_router(user_router, prefix="/v1")