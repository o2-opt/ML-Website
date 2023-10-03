# -*- coding: utf-8 -*-
"""
Created on Thu Mar 03 12:23 2023
@author: Otto

TODO:
add metric convertion option
add check for valid input
    TMAX > TAVG > TMIN
add SAHP statistics for given input

"""

from flask import Flask, render_template, request
import pickle
import numpy as np

import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import FeatureUnion
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from sklearn.linear_model import LinearRegression
def identity(x): return x

app     = Flask(__name__)
model   = pickle.load(open('main_pipeline.pk', 'rb'))
Columns = pickle.load(open('columns.pk', 'rb'))

# ['TAVG', 'TMAX', 'TMIN', 'PRCP', 'SNOW', 'SNWD', 'Holiday', 'weekend']

@app.route('/')
def man():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['TAVG']
    data2 = request.form['TMAX']
    data3 = request.form['TMIN']
    data4 = request.form['PRCP']
    data5 = request.form['SNOW']
    data6 = request.form['SNWD']

    try:
        request.form['Holiday']
        data7 = 1
    except: data7 = 0
    try:
        request.form['weekend']
        data8 = 1
    except: data8 = 0
    
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8]])
    arr = pd.DataFrame(arr,columns=Columns)
    pred = model.predict(arr)[0]
    pred = int(round(pred, 0))
    
    return render_template('after.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)








