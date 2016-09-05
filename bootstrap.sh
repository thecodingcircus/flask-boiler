#!/usr/bin/env bash

apt-get update
apt-get install -y python-dev python-pip git fabric python-mysqldb
mkdir -p /opt/projects
cd /opt/projects
git clone https://jaredhenry6@bitbucket.org/jaredhenry6/flask-boiler.git
cd flask-boiler
pip install -r requirements




