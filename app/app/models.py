from app import db


class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), unique=True, nullable=True)
    people = db.Column(db.Text)

    def __repr__(self):
        return "Meeting('{}')".format(self.date)
