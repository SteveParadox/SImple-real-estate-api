import os


class Config:
    ENV = 'dev'

    if ENV == 'dev':
        SQLALCHEMY_DATABASE_URI = 'sqlite:///db.api' #for development dababase
    else:

        SQLALCHEMY_DATABASE_URI = 'sqlite:///db.api'  #for production database 

    SECRET_KEY = 'something secret' #os.environ.get('SECRET_KEY') change later
    SQLALCHEMY_TRACK_MODIFICATIONS = True

