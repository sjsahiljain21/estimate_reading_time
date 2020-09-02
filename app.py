from flask import Flask, render_template, url_for, request
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import numpy as np

import os
path="C:\\Users\\HP\\Downloads\\reading_time_test"
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
        body_tokenized = body.split()
        reading_time = 'Estimated reading time: {} minutes'.format(round(len(body_tokenized) / 220))
    return render_template('home.html', prediction=reading_time)


if __name__ == '__main__':
    app.run(debug=True)