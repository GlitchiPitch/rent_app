from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID

from core.models import Base


class User(Base, SQLAlchemyBaseUserTableUUID):
    ...