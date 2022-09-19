from . import db
from datetime import date
import datetime

class Todo(db.Model):
  sno = db.Column(db.Integer(), primary_key= True)
  title = db.Column(db.String(200), nullable= False)
  desc = db.Column(db.String(500), nullable= False)
  date_created = db.Column(db.String(), default=(str(date.today()) + " ("+datetime.datetime.now().strftime("%A")+")") )
  #(str(date.today()) + " ("+datetime.datetime.now().strftime("%A")+")")  

  def __repr__(self) -> str:
     return f"{self.sno}-{self.title}"  