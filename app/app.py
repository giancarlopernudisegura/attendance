from flask import Flask, render_template
from forms import CreateAttendance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'FEDD82CFAC8127DDDF9A483EB95E7'


@app.route("/", methods=['GET', 'POST'])
@app.route("/create", methods=['GET', 'POST'])
def create():
    form = CreateAttendance()
    # if (f.validate()):
    #     return render_template('attendance.html', f=f)
    return render_template('create.html', f=form)


@app.route("/attendance")
def attendance():
    return render_template('attendance.html')


if (__name__ == '__main__'):
    app.run(debug=True)
