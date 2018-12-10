# made by Giancarlo Pernudi
from flask import render_template, url_for, flash, redirect
from app import app, db
from app.forms import CreateAttendance
from app.models import Meeting

# dummy data
members = ["Giancarlo Pernudi", "Justin Stevens",
           "Will Fenton", "Paul Saunders", "Peter Friedrich"]

# CHANGE IN FINAL
db.drop_all()
db.create_all()


@app.route("/", methods=['GET', 'POST'])
@app.route("/create", methods=['GET', 'POST'])
def create():
    form = CreateAttendance()
    if (form.validate_on_submit()):
        meeting = Meeting(date=form.entrydate.data)
        db.session.add(meeting)
        db.session.commit()
        flash('sign in sheet created for {}'.format(
            form.entrydate.data), 'success')
        return redirect(url_for('attendance'))
    return render_template('create.html', f=form)


@app.route("/attendance", methods=['GET', 'POST'])
def attendance():
    index = len(Meeting.query.all()) - 1
    print("> " + str(Meeting.query.all()[index].date))
    return render_template('attendance.html', members=members, m=Meeting.query.all()[index])
