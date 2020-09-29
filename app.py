# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 22:08:17 2020

@author: HP
"""

from flask import Flask, render_template, url_for, request
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize

import os
path="C:\\Users\\HP\\Downloads\\estimate_reading_time"
os.chdir(path)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        body = request.form['body']
        body = [body]
        body = pd.DataFrame({'body': body})
        body = body['body'][0]
        body_tokenized = word_tokenize(body)
        reading_time = 'Estimated reading time: {} minutes'.format(round(len(body_tokenized) / 250))
    return render_template('home.html', prediction=reading_time)


if __name__ == '__main__':
    app.run(debug=True)