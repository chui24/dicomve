from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from config import db


#Definiendo el modelo de la tabla users que cree para la base de datos 


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    last_login = Column(DateTime)



class UserConnection:
    conn = None
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)


    def write_user(self, data):
            try:
                db_data = User(**data)
                print("a")
                session = self.SessionLocal()
                print("aa")
                session.add(db_data)
                print("aaa")
                session.commit()
                print("aaaaa")
                return {'success': True, 'message': 'User successfully registered'}
            except IntegrityError:
                print("ee")
                session.rollback()
                return {'success': False, 'message': 'User already exists.'}
            except Exception as e:
                print(e)
                session.rollback()
                return {'success': False, 'message': f'Error trying to create user: {str(e)}'}
            finally:
                print("eeeee")
                session.close()