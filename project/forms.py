from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, HiddenField,PasswordField
from wtforms.validators import DataRequired


class registerForm(FlaskForm):
  email = StringField(label="Email", validators= [DataRequired()])
  password = PasswordField(label="Password", validators= [DataRequired()])
  conf_password = PasswordField(label="Confirm Password", validators= [DataRequired()])
  log_in = SubmitField(label="Register")


class loginForm(FlaskForm):
  email = StringField(label="Email", validators= [DataRequired()])
  password = PasswordField(label="Password", validators= [DataRequired()])
  log_in = SubmitField(label="Sign in")
 
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