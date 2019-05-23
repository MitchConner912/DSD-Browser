from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


curdate = datetime.today().strftime('%Y%m%d')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Mitch\\PycharmProjects\\RadioDB\\bpdcalls.db'
db = SQLAlchemy(app)

class BPDCalls(db.Model):
    __tablename__ = 'bpdcalls'
    date = db.Column(db.String)
    time = db.Column(db.String)
    duration = db.Column(db.Integer)
    type = db.Column(db.String)
    cc = db.Column(db.String) # Integer?
    slot = db.Column(db.String)
    calltype = db.Column(db.String)
    grp = db.Column(db.String)
    rid = db.Column(db.String)
    src = db.Column(db.String, primary_key=True)



@app.route('/', methods=['POST', 'GET'])
def index():
    calls = BPDCalls.query.all()
    callstoday = BPDCalls.query.filter_by(date=curdate).all()

    return render_template('index.html', calls=calls, callstoday=callstoday)

if __name__ == '__main__':
    app.run(debug=True)