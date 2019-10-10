# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
    
import sat_classifier as sc

if __name__=='__main__':
    X,Y = sc.return_sat_data(0)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 21)
    # Feature Scaling
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 42)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    print("-----LOGISTIC REGRESSION-----")
    model = LogisticRegression(solver = 'lbfgs', multi_class='ovr')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    ct = pd.crosstab(y_test, y_pred, rownames=['Actual Orbit'], colnames=['Predicted Orbit'])
    print(ct)
    print('Misclassified samples: {}'.format((y_test != y_pred).sum()))
    print('Accuracy: {}'.format(accuracy_score(y_test, y_pred)))
    print()
    print("Weight of parameters: ")
    print("[perigee, apogee, eccentricity, inclination, period]")
    print(model.coef_)