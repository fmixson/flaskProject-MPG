from datetime import datetime
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, redirect
from flask_migrate import Migrate
from forms import AddMPGForm, DelMPGForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

class MPG(db.Model):
    # __table__ = 'mpgs'

    id = db.Column(db.Integer, primary_key=True)
    current_mileage = db.Column(db.Integer)
    gallons_purchased = db.Column(db.Float)
    # date = db.Column(db.DateTime)
    # miles_driven = db.Column(db.Integer)
    # miles_per_gallon = db.Column(db.Integer)

    def __init__(self, current, gallons, date):
        self.current_mileage = current
        self.gallons_purchased = gallons
        # self.date = date

    def __repr__(self):
        return f'{self.current_mileage} and {self.gallons_purchased} on {self.date}'

@app.route('/')
def index():
    return render_template('home.html')

# app.route('/thankyou')
# def thankyou():
#     return render_template('thankyou.html')

@app.route('/add_mileage', methods=['GET', 'POST'])
def add_mileage():
    form = AddMPGForm()
    # today_date = datetime.date()
    previous_mileage = MPG.query.all()
    length = len(previous_mileage)
    pre_mileage = previous_mileage[length-1]

    if form.validate_on_submit():
        current_mileage = form.current_mileage.data
        gallons_purchased = form.gallons_purchased.data

        new_data = MPG(current=current_mileage, gallons=gallons_purchased)
        db.session.add(new_data)
        db.session.commit()

        return redirect(url_for('list_mileage'))
    return render_template('add_mileage.html', form=form, previous_mileage=pre_mileage.current_mileage)

@app.route('/list_mileage')
def list_mileage():
    mileage = MPG.query.all()
    print(mileage)

    return render_template('list.html', mileage=mileage)

if __name__ == '__main__':
    app.run(debug=True)
