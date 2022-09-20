from flask import Blueprint,render_template, request, redirect
from .forms import *
from .models import db,Todo
from flask_login import current_user,login_required

view = Blueprint('view',__name__)
 
@view.route("/", methods =['GET','POST'])
@view.route('/home')
@login_required
def home_page():
    form = todoForm()
    upform = todoUpdate()
    searchform = searchTodo()    
    if form.submit1.data and form.validate():      
        todo = Todo(title = form.title1.data, desc = form.desc1.data, user_id=current_user.id)    
        db.session.add(todo)
        db.session.commit()       
       
    if upform.submit2.data : 
       todo = Todo.query.filter_by(sno=upform.sno2.data, user_id=current_user.id).first()       
       todo.title = upform.title2.data
       todo.desc = upform.desc2.data 
       db.session.commit()

    if searchform.submit3.data : 
       todo = Todo.query.filter_by(title=searchform.search.data,user_id=current_user.id)
       print(current_user.id)
       res = []
       if todo!=None:  
        for task in todo:
          res.append(task)  
       alltodo= res    
       return render_template('index.html', todoList = alltodo, form=form, upform=upform, searchform=searchform, search=True)
 
    
    alltodo = Todo.query.filter_by(user_id=current_user.id)
    res=[]
    if alltodo!=None:  
      for task in alltodo:
         res.append(task)  
    alltodo= res  
    print(current_user.id)
    return render_template('index.html', todoList = alltodo, form=form, upform=upform, searchform=searchform, search=True)


@view.route('/delete/<int:sno>')
@login_required
def delete(sno):
  deltodo =  Todo.query.filter_by(sno=sno,user_id=current_user.id).first()
  db.session.delete(deltodo)
  db.session.commit()
  return redirect("/")

@view.route("/about")
def about():
  return render_template("about.html",search=False)