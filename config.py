import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:123456@localhost/dicomve')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
