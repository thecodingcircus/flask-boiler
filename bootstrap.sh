#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y python-dev python-pip git fabric python-mysqldb libffi-dev
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'
sudo apt-get -y install mysql-server redis-server
mkdir -p /opt/projects
cd /opt/projects
git clone https://jaredhenry6@bitbucket.org/jaredhenry6/flask-boiler.git
cd flask-boiler
pip install -r requirements.txt
pip install pymongo
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org




