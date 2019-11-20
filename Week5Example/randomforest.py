from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt
import numpy as np

#from plot_confusion_matrix import plot_confusion_matrix

data_bunch = load_iris()
x = data_bunch['data']
y = data_bunch['target']

x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.8)
forest_model = RandomForestClassifier(n_estimators=100, criterion="gini",verbose=1)
forest_model.fit(x_train, y_train)
predict = forest_model.predict(x_test)
print(accuracy_score(y_test, predict))
print(confusion_matrix(y_test, predict))
print(f1_score(y_test, predict))
print(f1_score(y_test, predict, average=None))