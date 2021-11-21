from flask import *
import os
# -*- coding: utf-8 -*-


# Flaskオブジェクトの生成
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run()