from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app2=Flask(__name__)
#database connectivity configuration code
app2.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flaskproject'
app2.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print("iran")
db=SQLAlchemy(app2)

#dbmodel
class user(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),nullable=True)
    email=db.Column(db.String(20),nullable=True)
    phone=db.Column(db.String(12),nullable=True)
    meg=db.Column(db.String(80),nullable=True)
with app2.app_context():
    db.create_all()

if __name__=="__main__":
    app2.run(debug=True)