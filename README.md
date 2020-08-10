# Overview

A simple API of real estate management business .

# Getting started

Please follow the instructions below.

Run manually:

* git clone REPO
* cd REPO
* python3 -m venv venv
* source venv/bin/activate
* pip3 install -r requirements.txt
* python3 run.py 

*You can then visit localhost:5000 to verify that it's running on your machine. Or, alternatively use postman*

Built to use with a frontend framework for data collection and operation.

To create a development database for the api

* cd REPO
* open terminal
* run python3 to enter console
* from base import db, create_app
* db.create_all(app=create_app)
