from Base import Base
from main.model.User import users


class UserService(Base):
    __model__ = users
userService = UserService()