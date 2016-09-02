from fabric.api import local, settings, abort
from fabric.contrib.console import confirm

# prepare for deployment

def set_dev():
    local('export APP_SETTINGS="project.server.config.DevelopmentConfig"')
def set_prod():
    local('export APP_SETTINGS="project.server.config.ProductionConfig"')

def create_db():
    """
    Initializes the creation of the DB.
    """
    local("python manage.py create_db")
    local("python manage.py db init")
    local("python manage.py db migrate")
    local("python manage.py create_admin")
    local("python manage.py create_data")

def install_requirements():
    local('pip install -r requirements.txt')

def setup_server():
    local('apt-get update')
    local('apt-get upgrade')
    local('apt-get -y install python-dev python-pip git python-mysqldb')
    install_requirements()


