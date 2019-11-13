from pandas import read_csv
from matplotlib import pyplot
from pandas.plotting import lag_plot
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error

sats = ['ABS-3A_40424_Inclination&SMA.csv',
'EUTELSAT_115_WEST_B_40425_Inclination&SMA.csv',
'EUTELSAT_8_WEST_B_40875_Inclination&SMA.csv',
'G25_24812_Inclination&SMA.csv',
'INMARSAT_5-F1_39476_Inclination&SMA.csv',
'INTELSAT_29E_IS-29E_41308_Inclination&SMA.csv',
'Intelsat28_37392_Inclination&SMA.csv',
'Satmex8_39122_Inclination&SMA.csv',
'Ses1_36516_Inclination&SMA.csv',
'Telstar401_22927_Inclination&SMA.csv']

for sat_name in sats:
	series = read_csv(sat_name, header=0, )
	# lag_plot(series[['Semi-major Axis (km)']])
	# pyplot.show()

	# split dataset
	X = series[['Semi-major Axis (km)']].values
	#X = series[['Inclination (deg)']].values
	#import pdb; pdb.set_trace()
	train, test = X[1:int(0.95 * len(X))], X[int(0.95*len(X)):]
	# train autoregression
	model = AR(train)
	model_fit = model.fit()
	print('Lag: %s' % model_fit.k_ar)
	#print('Coefficients: %s' % model_fit.params)
	# make predictions
	predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
	for i in range(len(predictions)):
		print('predicted=%f, expected=%f' % (predictions[i], test[i]))
	error = mean_squared_error(test, predictions)
	print('Test MSE: %.3f' % error)
	# plot results
	pyplot.figure(num=sat_name)
	pyplot.plot(test)
	pyplot.plot(predictions, color='red')
	pyplot.show()