from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField

class CoursesForm(FlaskForm):
    course = StringField('Course', [validators.DataRequired(), validators.Length(max=50)])
    coursedesc = StringField('Course Description', [validators.DataRequired(), validators.Length(max=50)])
    submit = SubmitField("Save")