# from sqlite3 import connect
from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnection:

    def __init__(self) -> None:
        self.__database_url = 'sqlite:///app/db/backend_test.db'
        self.__engine = self.__create_database_engine()
        self.session = self.__create_session()

    def __create_database_engine(self):
        engine = create_engine(self.__database_url, connect_args={
            "check_same_thread": False})
        return engine

    def __create_session(self):
        session_make = sessionmaker(bind=self.__engine)
        session = session_make()
        return session

    def get_engine(self):
        return self.__engine

    def get_session(self):
        return self.session
