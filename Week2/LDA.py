import pandas as pd
import numpy as np
import sat_classifier as sat
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

X,Y = sat.return_sat_data(0)
print(X)
print(Y)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = RandomForestClassifier(max_depth=2, random_state=0)

classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
print(cm)
print('Accuracy: ' + str(accuracy_score(y_test, y_pred)))

'''
print("-----LINEAR DETERMINANT ANALYSIS-----")
ct = pd.crosstab(y_test, y_pred, rownames=['Actual Orbit'], colnames=['Predicted Orbit'])
print(ct)
print('Misclassified samples: {}'.format((y_test != y_pred).sum()))
print('Accuracy: {}'.format(accuracy_score(y_test, y_pred)))
print()
print("Weight of parameters: ")
print("[perigee, apogee, eccentricity, inclination, period]")
print(classifier.feature_importances_)
'''