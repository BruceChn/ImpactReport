##project/users/views.py

#######################

from functools import wraps
from flask import Flask,flash,render_template,request,session,url_for,Blueprint,redirect
from .forms import LoginForm

users_blueprint = Blueprint('users',__name__)
### wrapper login_required decorator
def login_required(func):
	@wraps(func)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return func(*args,**kawrgs)
		else:
			flash('You need to login first:')
			return redirect(url_for('users.login'))
		return wrap

		
### routes

@users_blueprint.route('/',methods = ['GET','POST'])
def login():
	error = None
	form = LoginForm(request.form)
	
	if 'logged_in' in session:
		return redirect(url_for("overview.overview"))
	if request.method == 'POST':
		if form.validate_on_submit():
			if request.form['user'] == 'admin' and request.form['password'] == 'admin':
				session['logged_in'] = True
				flash('Welcome')
				redirect(url_for("overview.overview"))
			else:
				error = "Invalid username or password"
	return render_template('login.html',form = form,error = error)
