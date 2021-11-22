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
import os.path, time, re

# Flaskオブジェクトの生成
app = Flask(__name__)


@app.route("/")
def root():
    # HTMLでWebフォームを記述 --- (*2)
    return """
    <html>
    <head>
    <meta name="viewport" content="width=device-width,initial-scale=1">
    </head>
    </<body>
    <form action="/hello.html" method="post" target="_blank" >
      <input type="text" name="a">
      <input type="submit" value="計算" target="_blank">
    </form>
    """

bullets = [
    'テキスト1',
    'テキスト2',
    'テキスト3'
]


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
    citys = "komama"
    df = soup.find_all(re.compile("^h1|h2|h3|h4|h5|h6"))
    return render_template('hello.html', city=city, citys=citys, df=df)



# サーバーを起動
if __name__ == '__main__':
    app.run()