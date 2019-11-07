from pandas import read_csv
from matplotlib import pyplot
from pandas.plotting import lag_plot
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error

series = read_csv('EUTELSAT_8_WEST_B_40875_Inclination&SMA.csv', header=0, index_col=0)
lag_plot(series)
pyplot.show()

# split dataset
X = series.values
train, test = X[1:len(X)-10000], X[len(X)-10000:]
# train autoregression
model = AR(train)
model_fit = model.fit()
print('Lag: %s' % model_fit.k_ar)
print('Coefficients: %s' % model_fit.params)
# make predictions
predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
for i in range(len(predictions)):
	print('predicted=%f, expected=%f' % (predictions[i], test[i]))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot results
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()