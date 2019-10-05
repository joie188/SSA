# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 21:10:06 2019

@author: Brian
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import string
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
        
def can_be_floated(array):
    for i in array:
        if isinstance(i, float) or isinstance(i, int):
            if np.isnan(i):
                continue
            return False
        for char in i:
            if char not in '1234567890,':
                return False
        return True
        
def floatify(array):
    new_array = []
    for i in array:
        if isinstance(i, str):
            try:
                i = float(i.translate(str.maketrans('', '', string.punctuation)))
            except ValueError:
                pass
        new_array.append(i)   
    return new_array


def all_same(array):
    same_type = type(array[0])
    for i in array:
        if type(i) != same_type:
            return False
    return True

def random_forest(data, orbit):
    x = np.column_stack(data)[1:, 2:]       #independent variables (e, a, p, T)
    y = np.column_stack(data)[1:, orbit]    #class or type of orbit
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 21)
    # Feature Scaling
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 42)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    print("-----RANDOM FOREST-----")
    ct = pd.crosstab(y_test, y_pred, rownames=['Actual Orbit'], colnames=['Predicted Orbit'])
    print(ct)
    print('Misclassified samples: {}'.format((y_test != y_pred).sum()))
    print(accuracy_score(y_test, y_pred))
    print("[perigee, apogee, eccentricity, inclination, period]")
    print(classifier.feature_importances_)
    #ct.plot.bar(stacked=True)
    #plt.legend(title='Orbit')
    #plt.show()
    print()
    print("-----LOGISTIC REGRESSION-----")
    model = LogisticRegression(solver = 'lbfgs', multi_class='ovr')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    ct = pd.crosstab(y_test, y_pred, rownames=['Actual Orbit'], colnames=['Predicted Orbit'])
    print(ct)
    print('Misclassified samples: {}'.format((y_test != y_pred).sum()))
    print(accuracy_score(y_test, y_pred))
    print("[perigee, apogee, eccentricity, inclination, period]")
    print(model.coef_)

if __name__=='__main__':

    data = pd.read_csv("Week2_Problem2.csv")
    org_data = {}

    for i in data:
        if 'Unnamed' not in i and i != 'Comments' and 'Source' not in i:
            org_data[i] = [i for i in data[i]]

    for attr in org_data:
        data_list = org_data[attr]
        if can_be_floated(data_list):
            org_data[attr] = floatify(data_list)

    '''for attr in org_data:
        print(attr, type(org_data[attr][0]), all_same(org_data[attr]))
        print('--------------------')'''
    
    col_of_interest = {}
    data_as_mat = []
    for attr, val in org_data.items():
        if 'Orbit' in attr or 'Perigee' in attr or 'Apogee' in attr or 'Eccentricity' in attr or 'Inclination' in attr or 'Period' in attr:
            col_of_interest[attr] = val  
            data_as_mat.append([attr] + val) 
    random_forest(data_as_mat, 0)