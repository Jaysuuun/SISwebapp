from flask import render_template, redirect, request, flash
from . import student_bp
import webapp.models as models
from webapp.students.forms import StudentForm
from webapp import mysql

@student_bp.route('/students')
@student_bp.route('/')
@student_bp.route('/edit_students')

@student_bp.route('/')
def students_page():
    students = models.Students.all()
    return render_template('students/students.html', student = students)


@student_bp.route('/data_students', methods = ['POST','GET'])
def data_students_page():
    form = StudentForm()
    if request.method == 'POST' and form.validate():
        students = models.Students(idnumber = form.idnumber, fname=form.fname, mname=form.mname,lname= form.lname, gender=form.gender, yearlvl= form.yearlvl, course=form.course)
        students.add()
        return redirect('/')
    else:
        return render_template('students/data_students.html', form = form)

'''@student_bp.route('/edit_students/<idnumber>', methods = ['GET','POST'])
def edit_students_page(idnumber):
    data = models.Students.edit(idnumber)
    return render_template('students/edit_students_data.html', data = data)'''
