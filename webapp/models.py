from webapp import mysql

class Students(object):

    def __init__(self, idnumber=None, fname=None, mname=None, lname=None, gender=None, yearlvl=None, course=None):
        self.idnumber = idnumber
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.gender = gender
        self.yearlvl = yearlvl
        self.course = course

    def add(self):
        cursor = mysql.connection.cursor()

        sql = f"INSERT INTO data(idnumber,fname,mname,lname,gender,yearlvl,course) \
                VALUES('{self.idnumber}','{self.fname}','{self.mname}','{self.lname}','{self.gender}','{self.yearlvl}','{self.course}')" 

        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()
        sql = cursor.execute("SELECT * from data")
        if sql > 0:
            result = cursor.fetchall()
        return result

    @classmethod
    def edit(cls, idnumber):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * from data where STUDENTID = {idnumber}" 
        cursor.execute(sql)
        idnumber = cursor.fetch()
        return idnumber

    @classmethod
    def update(cls, idnumber):
        try:
            cursor = mysql.connection.cursor()
            sql = f"UPDATE from data where STUDENTID= {idnumber}"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False




    @classmethod
    def delete(cls,id):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from users where id= {id}"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False

class Courses(object):

    def __init__(self, course=None, coursedesc=None):
        self.course = course
        self.coursedesc = coursedesc

    def add(self):
        cursor = mysql.connection.cursor()

        sql = f"INSERT INTO courses(courses,coursdesc) \
                VALUES('{self.course}','{self.coursedesc}')" 

        cursor.execute(sql)
        mysql.connection.commit()
    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = f"SELECT * from courses"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def populate(cls):
        cursor = mysql.connection.cursor()

        sql = f"SELECT COURSEID from courses"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result