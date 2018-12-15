# made by Giancarlo Pernudi
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class CreateAttendance(FlaskForm):
    entrydate = DateField('Date: ', validators=[
        DataRequired()], format='%Y-%m-%d')
    submit = SubmitField('Create')
