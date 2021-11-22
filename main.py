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
      <input type="text" name="a" style="width:100%;">
      <input type="submit" value="計算" target="_blank" style="width:100%;margin-top: 10px;">
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
    links = soup.select("link[rel='canonical']")
    for e in links:
        xs = e.attrs["href"]
    desc = ""
    for meta in soup.findAll("meta"):
        metaname = meta.get('name', '').lower()
        metaprop = meta.get('property', '').lower()
        if 'description' == metaname or metaprop.find("description")>5000:
            desc = meta['content'].strip()
    ln2 = len(desc)
    for script in soup(["script", "style"]):
        script.extract() 
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    ln3 = len(text)
    return render_template('hello.html', ln3=ln3, citys=citys, df=df, xs=xs, a=a, desc=desc, ln2=ln2)



# サーバーを起動
if __name__ == '__main__':
    app.run()