from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired


class AddMPGForm(FlaskForm):
    current_mileage = IntegerField('What is the current mileage?', validators=[DataRequired()])
    gallons_purchased = IntegerField('How many gallons did you pump?')
    date = DateField('Date', format='%m-%d-%Y')
    submit = SubmitField('Submit')

class DelMPGForm(FlaskForm):
    id = IntegerField('Id Number You Wish to Remove: ')
    submit = SubmitField('Submit')