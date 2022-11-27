from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, SelectField
import webapp.models as models

year_level = ('1st Year','2nd Year','3rd Year','4th Year')
gengen = ('','Male','Female', 'Other')

class StudentForm(FlaskForm):
    idnumber = StringField('ID Number', [validators.DataRequired(), validators.Length(min=9, max=9)])
    fname = StringField('First Name', [validators.DataRequired(), validators.Length(max=50)])
    mname = StringField('Middle Name', [validators.Length(max=50)])
    lname = StringField('Last Name', [validators.DataRequired(), validators.Length(max=50)])
    gender = SelectField('Gender', choices=gengen)
    yearlvl = SelectField('Year Level', choices= year_level)
    course = SelectField('Course', choices= '')
    submit = SubmitField("Save")

