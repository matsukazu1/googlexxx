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
import bleach
import bleach
import requests
import codecs
from bs4 import BeautifulSoup
import urllib.parse
import os.path, time, re
import re
import requests
import urllib.parse
from bs4 import BeautifulSoup
from flask import Markup

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
      <input type="submit" value="計算!!" target="_blank" style="width:100%;margin-top: 10px;">
    </form>
    """



@app.route("/hello.html", methods=["post"])
def hello():
    numbers = 0
    a = str(request.form.get("a"))
    result = requests.get(f"https://www.google.co.jp/search?num=10&q=" + a + "&source=lnt&tbs=lr:lang_1ja&lr=lang_ja&sa=X&ved=2ahUKEwi1mO2n4qvpAhVMHaYKHUhYBfMQpwV6BAgOEBk&biw=1536&bih=674")
    soup = BeautifulSoup(result.text, 'html.parser')
    link_google = soup.select('.kCrYT > a')
    #print(link_google)
     #for i in range(len(link_google)):
      #print(link_google[i])
    ganba = []
    xs = []
    xn = []
    xn2 = []
    xn3 = []
    xx =[]
    for i in link_google:
        if "twitter.com" in str(i):
            print(1)
        elif "youtube.com" in str(i):
            print(1)
        elif "amazon.co.jp" in str(i):
            print(1)
        elif "facebook.com" in str(i):
            print(1)
        elif "instagram.com" in str(i):
            print(1)
        elif "wantedly.com" in str(i):
            print(1)
        elif "newspicks.com" in str(i):
            print(1)
        else:
            xx.append(i)
    print(xx)
    for i in range(len(xx)):
        #なんか変な文字が入るので除く
        site_url = xx[i].get('href').split('&sa=U&')[0].replace('/url?q=', '')
        #URLに日本語が含まれている場合、エンコードされているのでデコードする
        numbers += 1
        site_url = urllib.parse.unquote(urllib.parse.unquote(site_url))
        ganba.append(str(site_url))
    for ii in ganba:
        r = requests.get(ii, timeout=30)
        ii = str(r)
        xs.append(str("【URL】:" + ii))
        #xs.append(str("s"))
    for ii in ganba:
        site_url = urllib.parse.unquote(urllib.parse.unquote(ii))
        html = requests.get(site_url)
        html.encoding = html.apparent_encoding
        soup = BeautifulSoup(html.text, "html.parser")
        ps = soup.title.string
        for script in soup(["script", "style"]):
            script.extract() 
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        xx = len(text)
        xn.append(str(xx))
    return render_template('hello.html', link_google=link_google, ganba=ganba, xn=xn)

#いけた

# サーバーを起動
if __name__ == '__main__':
    app.run()