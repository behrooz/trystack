from os import environ


class Config:

     ENV = environ.get("TRYSTACK_API_ENV","production")
     DEBUG = environ.get("TRYSTACK_API_DEBUG", "0")
     TESTING = DEBUG

     SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI","mysql+pymysql://root:123@192.168.2.20:3316/trystack")
     SQLALCHEMY_RECORD_MODIFICATIONS = DEBUG
     SQLALCHEMY_RECORD_QUERIES = DEBUG
     SQLALCHEMY_ECHO = DEBUG