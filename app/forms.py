from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField
from wtforms.validators import DataRequired


class CreateAttendance(FlaskForm):
    entrydate = DateField('Date: ', validators=[
        DataRequired()], format='%Y-%m-%d')
    submit = SubmitField('Create')
