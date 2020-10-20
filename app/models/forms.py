from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
  
  email = StringField('Email', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])


class CadastroForm(FlaskForm):

  username = StringField('Name', validators=[DataRequired()])
  name = StringField('Name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])


class PostForm(FlaskForm):

	about = TextAreaField(validators=[DataRequired()])

class AlteracoesForm(FlaskForm):
  
  username = StringField('Name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
