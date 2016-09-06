# project/server/__init__.py


#################
#### imports ####
#################

import os

from flask import Flask, render_template
from flask_login import LoginManager, current_user
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin import helpers, expose
import flask_restless

################
#### config ####
################

app = Flask(
    __name__,
    template_folder='../client/templates',
    static_folder='../client/static'
)

app_settings = os.getenv('APP_SETTINGS', 'project.server.config.DevelopmentConfig')
app.config.from_object(app_settings)


####################
#### extensions ####
####################

login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
toolbar = DebugToolbarExtension(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


###################
### blueprints ####
###################

from project.server.user.views import user_blueprint
from project.server.main.views import main_blueprint
app.register_blueprint(user_blueprint)
app.register_blueprint(main_blueprint)


###################
### flask-login ####
###################

from project.server.models import User

login_manager.login_view = "user.login"
login_manager.login_message_category = 'danger'


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()

###################
### flask-admin ####
###################

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_admin()
admin = Admin(app, name='Flask Boiler', template_mode='bootstrap3', index_view=MyAdminIndexView())
# http://127.0.0.1:5000/admin
admin.add_view(ModelView(User, db.session, endpoint='UserEndpoint'))


###################
### flask-restless ####
###################
manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

# http://127.0.0.1:5000/api/users
manager.create_api(User, methods=['GET', 'POST', 'DELETE'])


########################
#### error handlers ####
########################

@app.errorhandler(401)
def forbidden_page(error):
    return render_template("errors/401.html"), 401


@app.errorhandler(403)
def forbidden_page(error):
    return render_template("errors/403.html"), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500
