from os import environ


class Config:

     ENV = environ.get("TRYSTACK_API_ENV","production")
     DEBUG = environ.get("TRYSTACK_API_DEBUG", "0")
     TESTING = DEBUG

     SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI","mysql+pymysql://root:123@localhost:3306/trystack")
     SQLALCHEMY_RECORD_MODIFICATIONS = DEBUG
     SQLALCHEMY_RECORD_QUERIES = DEBUG
     SQLALCHEMY_ECHO = DEBUG

     CACHE_TYPE = environ.get("CACHE_TYPE")
     CACHE_REDIS_HOST = environ.get("CACHE_REDIS_HOST","redis://localhost:6379")
     CACHE_REDIS_PORT = environ.get("CACHE_REDIS_PORT","6379")
     CACHE_REDIS_DB  = environ.get("CACHE_REDIS_DB")
     CACHE_REDIS_URL = environ.get("CACHE_REDIS_URL")
     CACHE_DEFAULT_TIMEOUT = environ.get("CACHE_DEFAULT_TIMEOUT")

