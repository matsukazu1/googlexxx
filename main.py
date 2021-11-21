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

# ルート( / )へアクセスがあった時 --- (*1)
@app.route("/")
def root():
    # HTMLでWebフォームを記述 --- (*2)
    return """
    <html><body>
    <form action="/calc" method="post">
      <input type="text" name="a"> ×
      <input type="text" name="b">
      <input type="submit" value="計算">
    </form>
    """

@app.route("/calc", methods=["post"])
def calc():
    a = str(request.form.get("a"))
    url = a
    # URLを開く
    #html = urllib.request.urlopen(url)
    # BeautifulSoupで開く
    # r = BeautifulSoup(html, "html.parser")
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "html.parser")
    return "<h1>答えは..." + str(bs) + "</h1>"

if __name__ == '__main__':
  app.run()