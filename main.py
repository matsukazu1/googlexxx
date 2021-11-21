from flask import *
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
import urllib.request
import requests
from bs4 import BeautifulSoup
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Heroku"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)