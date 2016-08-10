## project/__init__.py

from flask import Flask,render_template
from pymongo import MongoClient
app = Flask(__name__)
db = MongoClient("104.154.49.93:27017").tsog

from project.users.views import users_blueprint
#from project.progress.view import progress_blueprint
#from project.overview.view import overview_blueprint
app.config.from_pyfile('_config.py')
app.register_blueprint(users_blueprint)

#app.register(progress_blueprint)
#app.register(overview_blueprint)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'),404
