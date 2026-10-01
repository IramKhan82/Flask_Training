from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app3=Flask(__name__)
#database connectivity configuration code
app3.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flaskproject'
app3.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print("iran")
db=SQLAlchemy(app3)

#dbmodel
class employee(db.Model):
    EmpID=db.Column(db.Integer,primary_key=True)
    EmpName=db.Column(db.String(80),nullable=True)
    EmpEmail=db.Column(db.String(20),nullable=True)
    Empphone=db.Column(db.String(12),nullable=True)
    EmpComp=db.Column(db.String(80),nullable=True)
with app3.app_context():
    db.create_all()

if __name__=="__main__":
    app3.run(debug=True)