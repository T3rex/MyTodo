from flask import Blueprint,render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, HiddenField
from wtforms.validators import DataRequired
from .models import db,Todo



view = Blueprint('view',__name__)


class todoForm(FlaskForm):
  sno1 = StringField()
  title1 = StringField(label="Title", validators= [DataRequired()])
  desc1 = StringField(label="Description", validators=[DataRequired()])
  submit1 = SubmitField(label="Submit")

class todoUpdate(FlaskForm):
  sno2 = HiddenField()
  title2 = StringField(label="Title", validators= [DataRequired()])
  desc2 = StringField(label="Description", validators=[DataRequired()])
  submit2 = SubmitField(label="Update")
 
class searchTodo(FlaskForm):
  search = StringField(label="Search title")
  submit3 = SubmitField(label="Search")
 
@view.route("/", methods =['GET','POST'])
@view.route('/home')
def home_page():
    form = todoForm()
    upform = todoUpdate()
    searchform = searchTodo()    
    if form.submit1.data and form.validate():      
        todo = Todo(title = form.title1.data, desc = form.desc1.data )    
        db.session.add(todo)
        db.session.commit()
        
       
    if upform.submit2.data : 
       todo = Todo.query.filter_by(sno=upform.sno2.data).first()       
       todo.title = upform.title2.data
       todo.desc = upform.desc2.data 
       db.session.commit()

    if searchform.submit3.data : 
       todo = Todo.query.filter_by(title=searchform.search.data)
       res = []
       if todo!=None:  
        for task in todo:
          res.append(task)  
       alltodo= res    
       return render_template('index.html', todoList = alltodo, form=form, upform=upform, searchform=searchform)
 
    alltodo = Todo.query.all() 
    return render_template('index.html', todoList = alltodo, form=form, upform=upform, searchform=searchform)


@view.route('/delete/<int:sno>')
def delete(sno):
  deltodo =  Todo.query.filter_by(sno=sno).first()
  db.session.delete(deltodo)
  db.session.commit()
  return redirect("/")

@view.route("/about")
def about():
  return render_template("about.html")



   