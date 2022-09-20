from . import db
from datetime import date
import datetime 
from flask_login import UserMixin

class Todo(db.Model):
  sno = db.Column(db.Integer(), primary_key= True)
  title = db.Column(db.String(200), nullable= False)
  desc = db.Column(db.String(500), nullable= False)
  date_created = db.Column(db.String(), default=(str(date.today()) + " ("+datetime.datetime.now().strftime("%A")+")") )
  user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
  #(str(date.today()) + " ("+datetime.datetime.now().strftime("%A")+")")  

  def __repr__(self) -> str:
     return f"{self.sno}-{self.title}"  

class User(db.Model,UserMixin):
  id= db.Column(db.Integer(), primary_key= True)
  email = db.Column(db.String(200),nullable=False, unique=True)
  password = db.Column(db.String(500),nullable=False)
  todos = db.relationship('Todo')
