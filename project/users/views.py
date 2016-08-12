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
@users_blueprint.route('/overview')
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
				'y':-70,
				'borderWidth':0,
				'useHTML':True
			}
		}
	}
	series3 = [{
		'enableMouseTracking': False,
		'name':'percentage',
		'data':[20],
		'dataLabels':{
			'format':r'<div style = \"text-align:center;\"><span style =\"font-size:35px;\">{y}%</span></div>'
		},
		'tooltip':{
			'valueSuffix':'%'
		}
	}]
	title3 = {
		'text':"Regional Average Comparison"
	}
	series4 = [{
		'name' :'Users',
		'color':'#FFA500',
		'data' : [400,799,1200,500,200,100]
	},
	{
		'name' :'Regional Average(Taken from statiscal Data)',
		'color' : "#00BFFF",
		'data':[200,300,500,700,600,500]
	}]

	overview_options = json.dumps(createOptions(credits,barchart,title1,xAxis1,yAxis1,series1)).replace("'",r"\'")
	average_comparion_options = json.dumps(createOptions(credits,barchart,title2,xAxis1,yAxis1,series2)).replace("'",r"\'")
	percentage_options1 = createOptions(credits,solidgauge,None,None,yAxis2,series3,pane)
	percentage_options1['plotOptions'] = plotOptions
	percentage_options1['tooltip'] = tooltip

	percentage_options2 = percentage_options1
	percentage_options1 = json.dumps(percentage_options1).replace("'",r"\'")
	regional_average_options = json.dumps(createOptions(credits,barchart,title3,xAxis1,yAxis1,series4)).replace("'",r"\'")


	percentage_options2['yAxis']['title']['text'] = "Bruce Chan is ranking in the 80 percentile"
	percentage_options2['series'][0]['data'][0] = 80
	percentage_options2 = json.dumps(percentage_options2).replace("'",r"\'")
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
	return render_template('overview.html',form = form,error = error,overview_options = overview_options,average_comparion_options = average_comparion_options,percentage_options1 = percentage_options1,regional_average_options = regional_average_options,percentage_options2 = percentage_options2)


@users_blueprint.route('/progresstracker')
def progresstrack():
	credits = {
		'enabled':False
	}
	semidonut = {
		'type':'pie'
	}
	title ={
		'text':'Level 1 Training Program',
		'align': 'center',
		'verticalAlign':'top',
		'y':35
	}
	tooltip = {
		'pointFormat':'{series.name}: <b>{point.percentage:.lf}%</b>'
	}
	plotOptions={
		'pie':{
			'dataLabels':{
				'enabled':True,
				'distance':-50,
				'style':{
					'fontWeight':'bold',
					'color':'white',
					'textShadow':'0px 1px 2px black'
				}
			},
			'startAngle':-90,
			'endAngle':90,
			'center':['50%',"75%"],
			'size':'125%'
		}
	}
	subtitle = {
		'verticalAlign':'middle',
		'align':'center',
		'text' : "Level 1",
		'y' : 85,
		'style':{
			'font-size':'35px',
			'fontWeight':'bold'
		}
	}
	series = [{
		'name':'Progress',
		'data':[
			['Reading',30],
			['Math',32],
			['Science',18],
			['Writing',20]
		],
		'innerSize':'45%',
		'dataLabels':{
            'format': r'<div style = \"text-align:center;\"><span style = \"font-size:35px\">{point.name}-{point.percentage:.lf}%</span></div>'
		}
    }]
	progress = createOptions(credits,semidonut,title,None,None,series)
	progress['plotOptions'] = plotOptions
	progress['tooltip'] = tooltip
	progress['subtitle'] = subtitle
	progress = json.dumps(progress).replace("'",r"\'")
	title['text'] = 'Overall'

	plotOptions1 =  {
                'pie': {
                    'allowPointSelect': True,
                    'cursor': 'pointer',
                    'dataLabels': {
                        'enabled': False
                    },
                    'showInLegend': True,
					'center':['50%',"50%"],
					'size':'75%'
                }
            }
	series1 = [{
		'name':'Progress',
		'colorByPoint':True,
		'innerSize':'50%',
		'data':[{
			'name':'Percentage Complete',
			'y':25,
			'color':'#FFA500'
		},{
			'name':'Percentage Remaining',
			'y':75,
			'color':'#87CEFA'
		}]
	}]
	overall = createOptions(credits,semidonut,title,None,None,series1)
	overall['tooltip'] = tooltip

	overall['plotOptions'] = plotOptions1
	math = overall
	reading = overall
	writing = overall
	science = overall
	overall = json.dumps(overall).replace("'",r"\'")
	math['title']['text'] = "Math"
	math['series'][0]['data'][0]['y'] = 60
	math['series'][0]['data'][1]['y'] = 40
	math = json.dumps(math).replace("'",r"\'")
	science['title']['text'] = "Science"
	science['series'][0]['data'][0]['y'] = 70
	science['series'][0]['data'][1]['y'] = 30
	science = json.dumps(science).replace("'",r"\'")
	reading['title']['text'] = "Reading"
	reading['series'][0]['data'][0]['y'] = 25
	reading['series'][0]['data'][1]['y'] = 75
	reading = json.dumps(reading).replace("'",r"\'")

	writing['title']['text'] = "Writing"
	writing['series'][0]['data'][0]['y'] = 55
	writing['series'][0]['data'][1]['y'] = 45
	writing = json.dumps(writing).replace("'",r"\'")
	return render_template('progresstracker.html',progress = progress,overall = overall,math = math,science = science,reading = reading,writing = writing)

@users_blueprint.route('/report')
def report():
	credits = {
		'enabled':False
	}
	chart = {
		'type':'line'
	}
	title = {
		'text':'Trending Report',
		'align' : 'center',
		'style' :{'fontSize':'2.5em','color':'#808080'}
	}
	xAxis = {
		'categories':['Week1','Week2','Week3','Week4','Week5','Week6','Week7','Week8','Week9']
	}
	yAxis = {
		'title':{
			'text' : 'Score'
		},
		'plotLines':[{
			'value':0,
			'width':1,
			'color':'#808080'
		}]
	},
	series = [{
		'name':'Overall',
		'data':[120,160,200,250,400,500,600,700,800]
	},{
		'name':'Reading',
		'data':[80,90,100,150,200,300,400,650,675]
	},{
		'name':'Math',
		'data':[150,180,220,270,410,550,675,725,845]
	},{
		'name':'Writing',
		'data':[125,190,250,300,350,400,425,517,627]
	},{
		'name':'Science',
		'data':[200,280,350,410,480,500,510,620,715]
	}]
	report = json.dumps(createOptions(credits,chart,title,xAxis,yAxis,series)).replace("'",r"\'")
	return render_template("report.html",report = report)
