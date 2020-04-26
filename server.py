# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:17:33 2020

@author: Neil

Creating a simple web server for heroku
"""

from os import environ
from flask import Flask

app = Flask(__name__)
app.run(host= '0.0.0.0', port=environ.get('PORT'))