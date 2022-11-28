from flask import Flask
from flask_mysqldb import MySQL,MySQLdb
from config import DB_HOST,DB_PORT,DB_NAME,DB_USERNAME,DB_PASSWORD,SECRET_KEY #SQLALCHEMY_DATABASE_URI
from flask_wtf.csrf import CSRFProtect

mysql = MySQL()

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
    MYSQL_HOST = DB_HOST,
    port = DB_PORT,
    MYSQL_DB = DB_NAME,
    MYSQL_USERNAME = DB_USERNAME,
    password = DB_PASSWORD,
    SECRET_KEY = SECRET_KEY,
    )

    mysql.init_app(app)
    CSRFProtect(app)

    from .students import student_bp as students_blueprint
    app.register_blueprint(students_blueprint)

    from .courses import course_bp as courses_blueprint
    app.register_blueprint(courses_blueprint)

    return app