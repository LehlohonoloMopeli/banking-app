from sqlalchemy import create_engine, connectors
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
import mysql.connector, pymysql

Base = declarative_base()

from .user import User
from .bank_accounts import BankAccounts
from .transactions import Transactions

engine = create_engine("mysql+pymysql://root:@127.0.0.1/banking-app", echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

connection = engine.connect()
