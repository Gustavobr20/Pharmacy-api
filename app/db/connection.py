# from sqlite3 import connect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


class DBConnection:

    def __init__(self) -> None:

        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        DB_PATH = os.path.join(ROOT_DIR, 'backend_test.db')

        self.__database_url = 'sqlite:///' + DB_PATH
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
