from sqlalchemy import *
from .user_schema import UserModel
from datetime import datetime


class Users(Base):

    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    timestamp = Column(DateTime, default=datetime.now())

    @staticmethod
    def exist(*args, **kwargs):
        return session.query(Users).filter(*args, **kwargs).first()

    @staticmethod
    def fromModel(user : UserModel):
        return Users(
            name=user.name,
            email=user.email
        )
    
    def toModel(self):
        return UserModel(
            id=self.id,
            name=self.name,
            email=self.email,
        )
    
    @staticmethod
    def create_user(user: UserModel):
        user_exists = Users.exist(Users.email == user.email)
        if user_exists:
            return None
        user_created = Users.from_model(user)
        session.add(user_created)
        session.commit()
        return user_created
    
    @staticmethod
    def get_users(limit, page):
        return session.query(Users).limit(limit).offset(limit * page)
