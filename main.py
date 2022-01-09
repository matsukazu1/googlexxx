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

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
header = {
    'User-Agent': user_agent
}

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
      <input type="text" name="a" style="width:100%;" placeholder="検索キーワードを入力">
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
        elif "rakuten" in str(i):
            print(1)
        elif "yahoo.co.jp" in str(i):
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
        r = requests.get(ii, timeout=59)
        ii = str(r)
        xs.append(str("【URL】:" + ii))
        #xs.append(str("s"))
    for ii in ganba:
        site_url = urllib.parse.unquote(urllib.parse.unquote(ii))
        r = requests.get(site_url, timeout=59)
        r.status_code
        rs = r.text
        content_type_encoding = r.encoding if r.encoding != 'ISO-8859-1' else None
        soupz = BeautifulSoup(r.content, 'html.parser', from_encoding=content_type_encoding)
        xx2 = str(soupz.title.string)
        xx = xx2
        xn.append(str(xx))
        xn3.append(Markup("<td>"))
        df = soupz.find_all(re.compile("^h1|h2|h3|h4|h5|h6"))
        for htag in df:
            if (r"<(h1|h2|h3|h4|h5|h6)"):
                i = htag
                i = str(i).replace('\n', "")
                i = str(i).replace('\r\n', "")
                i = str(i).replace('　', "")
                i = str(i).replace(' ', "")
                i = str(i).replace(' ', "")
                df = str(i).replace(' ', "")
                cd =  df.encode('cp932', "ignore")
                po = cd.decode('cp932')
                if "<h1" in po:
                    if "alt=" in po: 
                        xn3.append("【h1(alt)】" + re.search('(?<=alt=").*?(?=\")', (po)).group())
                        xn3.append(Markup("<br>"))
                    else:
                        xn3.append("【h1】" + bleach.clean(str(po), strip=True))
                        xn3.append(Markup("<br>"))
                elif "<h2" in po:
                    if "alt=" in po: 
                        xn3.append("【h2(alt)】" + re.search('(?<=alt=").*?(?=\")', (po)).group())
                        xn3.append(Markup("<br>"))
                    else:
                        xn3.append("【h2】" + bleach.clean(str(po), strip=True))
                        xn3.append(Markup("<br>"))
            else:None
        xn3.append(Markup("</td>"))
        #下をやってるよ
        #site_url = urllib.parse.unquote(urllib.parse.unquote(ii))
        #r = requests.get(site_url, timeout=59)
        #r.status_code
        #rs = r.text
        #content_type_encoding = r.encoding if r.encoding != 'ISO-8859-1' else None
        #soupz = BeautifulSoup(r.content, 'html.parser', from_encoding=content_type_encoding)
        #上をやってるよ
    for ii in ganba:
        site_url = urllib.parse.unquote(urllib.parse.unquote(ii))
        r = requests.get(site_url, timeout=59)
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
    return render_template('hello.html', link_google=link_google, ganba=ganba, xs=xs, xn=xn, xn2=xn2, xn3=xn3)

#いけた

# サーバーを起動
if __name__ == '__main__':
    app.run()