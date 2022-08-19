from typing import Any
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base: Any = declarative_base()

class Users:

    __tablename__ = "USERS"

    UUID = Column(String, primary_key=True)
    USERNAME = Column(String, nullable=False)
    PASSWORD = Column(String, nullable=False)