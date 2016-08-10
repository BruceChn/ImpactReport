##project/users/views.py

#######################

from functools import wraps
from flask import Flask,flash,render_template,request,session,url_for,Blueprint,redirect
from .forms import LoginForm
from project import db
import json

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


#createChartOptions
def createOptions(credits,chart,title,xAxis,yAxis,series,pane = None):
	options = {}
	options['credits'] = credits
	options['chart'] = chart
	options['title'] = title
	options['xAxis'] = xAxis
	options['yAxis'] = yAxis
	options['series'] = series
	options['pane'] = pane
	return options

### routes
@users_blueprint.route('/',methods = ['GET','POST'])
def overview():
	error = None
	form = LoginForm(request.form)
	credits = {'enabled':False}
	barchart = {'type':'bar'}
	title1 = {'text':"User's Overview"}
	xAxis1 = {
		'categories':['Writing Score','Science Score','Math Score','Reading Score','Current Overall Score','Best Overall Score To Date'],
		'title':{
			'text':None
			}
	}
	yAxis1 = {
		'min':0,
		'title':{
			'text':None
		},
		'max':1200
	}
	series1 = [{
		'showInLegend':False,
		'name':"score",
		'data': [{
			'y':200,
			'color':'#A9A9A9'
			},
			{
			'y':400,
			'color':'#A9A9A9'
			},
			{
				'y':500,
				'color':'#A9A9A9'
			},
			{
				'y':600,
				'color':'#A9A9A9'
			},
			{
				'y':900,
				'color':'#1E90FF'
			},
			{
				'y':1100,
				'color':'#6B8E23'
		}]

	}]
	title2 = {'text':"Organizational/School Average Comparion"}
	series2 = [{
		'name' : "Users",
		'color': "#FFA500",
		'data' :[800,900,400,590,699,700]
	},
	{
		'name' : "Average of Group Users",
		'color': "#00BFFF",
		'data' :[800,500,1000,220,699,700]
	}]
	solidgauge = {'type':'solidgauge'}
	pane = {
		'center':["50%","85%"],
		'size':"140%",
		'startAngle':-90,
		'endAngle':90,
		'background':{
			'backgroundColor':'#EEE',
			'innerRadius':'60%',
			'outerRadius':'100%',
			'shape':'arc'
		}
	}
	tooltip = {
		'enabled':False,

	}
	yAxis2 = {
		'stops':[
			[0.1,'#55BF3B'],
			[0.5,'#DDDF0D'],
			[0.9,'#DF5353']
		],
		'lineWidth':0,
		'minorTickInterval':None,
		'tickAmount':2,
		'title':{
			'text':'Bruce Chan is ranking in the 50 percentile',
			'y':-150
		},
		'labels':{
			'y':16
		},
		'min': 0,
		'max': 100
	}
	plotOptions = {
		'solidgauge':{
			'dataLabels':{
				'y':5,
				'borderWidth':0,
				'useHTML':True
			}
		}
	}
	series3 = [{
		'enableMouseTracking': False,
		'name':'percentage',
		'data':[80],
		'tooltip':{
			'valueSuffix':'%'
		}
	}]

	overview_options = json.dumps(createOptions(credits,barchart,title1,xAxis1,yAxis1,series1)).replace("'",r"\'")
	average_comparion_options = json.dumps(createOptions(credits,barchart,title2,xAxis1,yAxis1,series2)).replace("'",r"\'")
	percentage_options1 = createOptions(credits,solidgauge,None,None,yAxis2,series3,pane)
	percentage_options1['plotOptions'] = plotOptions
	percentage_options1['tooltip'] = tooltip
	percentage_options1 = json.dumps(percentage_options1).replace("'",r"\'")
	print percentage_options1
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
	return render_template('overview.html',form = form,error = error,overview_options = overview_options,average_comparion_options = average_comparion_options,percentage_options1 = percentage_options1)
