from os import getenv

DB_HOST=getenv("DB_HOST")
DB_PORT=getenv("DB_PORT")
DB_NAME=getenv("DB_NAME")
DB_USERNAME=getenv("DB_USERNAME")
DB_PASSWORD= getenv("DB_PASSWORD")
SECRET_KEY = getenv("SECRET_KEY")
#SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")