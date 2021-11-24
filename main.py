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
    result = requests.get(f"https://www.google.co.jp/search?num=10&q=猫&source=lnt&tbs=lr:lang_1ja&lr=lang_ja&sa=X&ved=2ahUKEwi1mO2n4qvpAhVMHaYKHUhYBfMQpwV6BAgOEBk&biw=1536&bih=674")
    soup = BeautifulSoup(result.text, 'html.parser')
    link_google = soup.select('.kCrYT > a')
    #print(link_google)
     #for i in range(len(link_google)):
      #print(link_google[i])
    ganba = []
    xs = []
    xn = []
    xn2 = []
    ganba2 = []
    for i in range(len(link_google)):
        #なんか変な文字が入るので除く
        site_url = link_google[i].get('href').split('&sa=U&')[0].replace('/url?q=', '')
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
        r = requests.get(site_url, timeout=30)
        r.status_code
        rs = r.text
        content_type_encoding = r.encoding if r.encoding != 'ISO-8859-1' else None
        soupz = BeautifulSoup(r.content, 'html.parser', from_encoding=content_type_encoding)
        xx2 = str(soupz.title.string)
        xx = xx2
        xn.append(str(xx))
    for ii in ganba:
        site_url = urllib.parse.unquote(urllib.parse.unquote(ii))
        r = requests.get(site_url, timeout=30)
        r.status_code
        rs = r.text
        content_type_encoding = r.encoding if r.encoding != 'ISO-8859-1' else None
        soup = BeautifulSoup(r.content, 'html.parser', from_encoding=content_type_encoding)
        desc = ""
        for meta in soup.findAll("meta"):
            metaname = meta.get('name', '').lower()
            metaprop = meta.get('property', '').lower()
            if 'description' == metaname or metaprop.find("description")>5000:
                desc = meta['content'].strip()
        xx = desc
        xn2.append(str(xx))
    #for ii in ganba:
    #    site_url = urllib.parse.unquote(urllib.parse.unquote(ii))
    #    r = requests.get(site_url, timeout=30)
    #    soup = BeautifulSoup(r.content, 'html.parser', from_encoding=content_type_encoding)
    #    df = soup.find_all(re.compile("^h1|h2|h3|h4|h5|h6"))
    #    for htag in df:
    #        if (r"<(h1|h2|h3|h4|h5|h6)"):
    #            i = htag
    #            i = str(i).replace('\n', "")
    #            i = str(i).replace('\r\n', "")
    #            i = str(i).replace('　', "")
    #            i = str(i).replace(' ', "")
    #            i = str(i).replace(' ', "")
    #            df = str(i).replace(' ', "")
    #            cd =  df.encode('cp932', "ignore")
    #            po = cd.decode('cp932')
    #            if "<h1" in po:
    #                if "alt=" in po: 
    #                    ganba2.append("【h1(alt)】" + re.search('(?<=alt=").*(?=\")', (po)).group())
    #                else:
    #                    ganba2.append("【h1】" + bleach.clean(str(po), strip=True))
    #        else:None
    return render_template('hello.html', link_google=link_google, ganba=ganba, xs=xs, xn=xn, xn2=xn2)

#いけた

# サーバーを起動
if __name__ == '__main__':
    app.run()