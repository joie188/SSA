import pandas as pd
import string
import numpy as np
import random

from sklearn import svm
from sklearn.model_selection import train_test_split
import sklearn.preprocessing
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

import sat_classifier as sc


if __name__ == "__main__":
    X,Y = sc.return_sat_data(0)

    #train-test split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=21)

    #feature scaling
    scaler = sklearn.preprocessing.StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)


    #fitting the model
    svc = svm.SVC(C=1,kernel='linear', decision_function_shape='ovr')
    svc.fit(X_train, Y_train)

    #testing the model
    Y_pred = svc.predict(X_test)

    print("--------SVM---------")
    print(pd.crosstab(Y_test, Y_pred, rownames=['Actual Orbit'], colnames=['Predicted Orbit']))
    print('Misclassified samples: {}'.format((Y_test != Y_pred).sum()))
    print('Accuracy: {}'.format(accuracy_score(Y_test, Y_pred)))

