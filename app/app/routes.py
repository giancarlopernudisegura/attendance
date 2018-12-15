# made by Giancarlo Pernudi
from flask import render_template, url_for, flash, redirect, request
from app import app, db
from datetime import date
from app.forms import CreateAttendance
from app.models import Meeting
from app.sheets import *

# member data
members = members()

# CHANGE IN FINAL
# db.drop_all()
# db.create_all()


@app.route("/", methods=['GET', 'POST'])
@app.route("/create", methods=['GET', 'POST'])
def create():
    form = CreateAttendance()
    if (form.validate_on_submit()):
        meeting = Meeting(date=form.entrydate.data)
        if (len(Meeting.query.filter_by(date=meeting.date).all()) == 0):
            db.session.add(meeting)
            db.session.commit()
            flash('sign in sheet created for {}'.format(
                form.entrydate.data), 'success')
        return redirect(url_for('attendance', fdate=str(meeting.date)))
    return render_template('create.html', f=form)


@app.route("/attendance/<fdate>", methods=['GET', 'POST'])
def attendance(fdate):
    return render_template('attendance.html', members=members, m=Meeting.query.filter_by(date=fdate).first())


@app.route("/send/<fdate>", methods=['POST'])
def send(fdate):
    list = []
    for m in members:
        if (request.form.get(m)):
            list.append(str(request.form.get(m)))
    sqlList = ','.join(list)
    m = Meeting.query.filter_by(date=fdate).first()
    m.people = sqlList
    db.session.commit()
    return "<h1>SUBMITTED " + str(Meeting.query.filter_by(date=fdate).first().date) + "</h1><a href='/create'>Make New Attendance Sheet</a>"
