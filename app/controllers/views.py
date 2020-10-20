from app import letstalk,db,login_m
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, request, redirect, url_for, session

from app.models.forms import LoginForm, CadastroForm, PostForm, AlteracoesForm
from app.models.tables import *

@login_m.user_loader
def load_user(id):
  return User.select().filter(id=id)

@letstalk.route('/')
def index():
	return render_template('index.html')


@letstalk.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():

		user = User.get(email=form.email.data)
		if user.password == form.password.data:
			login_user(user)
			return redirect(url_for("home"))
	else:
		print(form.errors)
		print('não válido')
	return render_template('login.html', form=form)


@letstalk.route('/cadastro', methods=['GET','POST'])
def cadastro():

  form = CadastroForm()
  if form.validate_on_submit():

    user = User.create(username=form.username.data, name=form.name.data, email=form.email.data, password=form.password.data)
    
    return redirect(url_for('login'))
  else:
    print(form.errors)
  return render_template('cadastro.html', form=form)


@letstalk.route('/perfil/<int:id>', methods=['GET', 'POST'])
def perfil(id):
	user = User.get(id=id)
	post = Post.select()
	return render_template('perfil.html', user=user) #post=post


@letstalk.route('/perfil/<int:id>/config', methods=['GET', 'POST'])
def config(id):
	form = AlteracoesForm()

	user = User.get(id=id)

	if form.validate_on_submit():
		
		user = User.get(id=id)

		user.email = form.email.data
		user.username = form.username.data
		user.password = form.password.data

		return redirect(url_for("config", user=user, id=id))

	return render_template('config.html', form=form, user=user)


@letstalk.route('/home', methods=['GET', 'POST'])
def home():
	id = current_user.get().id
	try:
		user = current_user.get()
		form = PostForm(request.form)
		
		if form.validate_on_submit():
			Post.create(about=form.about.data, user_id=user.id)
		else:
			print(form.errors)
		return render_template('home.html', form=form, user=user, id=id)
	except:
		return redirect(url_for('index'), id=id)


@letstalk.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))


@letstalk.route('/publicar', methods=['GET', 'POST'])
def publicar():
  print(request.form['mensagem'])
  return render_template('home.html')
