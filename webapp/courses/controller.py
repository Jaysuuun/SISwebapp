from flask import render_template, redirect, request
from . import course_bp
import webapp.models as models
from webapp.courses.forms import CoursesForm

@course_bp.route('/courses')
@course_bp.route('/courses/')

@course_bp.route('/courses/')
def course_page():
    courses = models.Courses.all()
    return render_template('courses/courses.html', course = courses )

@course_bp.route('/data_courses', methods = ['POST','GET'])
def data_courses_page():
    form = CoursesForm()
    if request.method == 'POST' and form.validate():
        courses = models.Courses(course = form.course, coursedesc=form.coursedesc)
        courses.add()
        return redirect('/courses/')
    else:
        return render_template('courses/data_courses.html', form = form)
