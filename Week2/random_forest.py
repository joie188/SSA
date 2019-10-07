# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
    
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