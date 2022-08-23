from typing import Any
from sqlalchemy import Column, String, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base: Any = declarative_base()


class Patients(Base):

    __tablename__ = "PATIENTS"

    UUID = Column(String, primary_key=True)
    FIRST_NAME = Column(String, nullable=False)
    LAST_NAME = Column(String, nullable=False)
    DATE_OF_BIRTH = Column(DateTime, nullable=False)


class Pharmacies(Base):

    __tablename__ = "PHARMACIES"

    UUID = Column(String, primary_key=True)
    NAME = Column(String, nullable=False)
    CITY = Column(String, nullable=False)


class Transactions(Base):

    __tablename__ = "TRANSACTIONS"

    UUID = Column(String, primary_key=True)
    PATIENT_UUID = Column(String)
    PHARMACY_UUID = Column(String)
    AMOUNT = Column(Numeric, nullable=False)
    TIMESTAMP = Column(DateTime, nullable=False)


class Users(Base):

    __tablename__ = "USERS"

    UUID = Column(String, primary_key=True)
    USERNAME = Column(String, nullable=False)
    PASSWORD = Column(String, nullable=False)
