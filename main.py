from flask import Flask
import os
from flask import *
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
import urllib.request
import requests
from bs4 import BeautifulSoup
from flask import Flask
import os
# -*- coding: utf-8 -*-

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Heroku"

if __name__ == '__main__':
  app.run()