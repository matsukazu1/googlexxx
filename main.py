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
from flask import Flask, render_template
from flask import render_template

# Flaskオブジェクトの生成
app = Flask(__name__)


@app.route("/")
def root():
    # HTMLでWebフォームを記述 --- (*2)
    return """
    <html><body>
    <form action="/hello.html" method="post">
      <input type="text" name="a">
      <input type="submit" value="計算">
    </form>
    """

@app.route("/hello.html", methods=["post"])
def hello():
    a = str(request.form.get("a"))
    url = a
    # URLを開く
    #html = urllib.request.urlopen(url)
    # BeautifulSoupで開く
    # r = BeautifulSoup(html, "html.parser")
    html = requests.get(url)
    html.encoding = html.apparent_encoding
    soup = BeautifulSoup(html.text, "html.parser")
    ps = soup.title.string
    city = str(ps)
    return render_template('hello.html', city=city)


# サーバーを起動
if __name__ == '__main__':
    app.run()