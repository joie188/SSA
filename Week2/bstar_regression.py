# Created by Luke de Castro, 10/9/19


import numpy
import pandas as pd
import matplotlib.pyplot as plt
import random
import string

import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import sklearn.preprocessing

import scipy.optimize

data = pd.read_csv("Week2_Problem3.csv")

epoch = data['EPOCH_MICROSECONDS'].to_numpy()
bstar = data['BSTAR'].to_numpy()

y = []
for s in bstar:
	y.append(s)

X = epoch
#y = bstar

def sin_func(sin_param, x):
	return (sin_param["amp"] * numpy.sin(sin_param['omega']*x + sin_param["offset"]) + sin_param['freq'])

def fit_sin(tt, yy):
    '''Fit sin to the input time sequence, and return fitting parameters "amp", "omega", "phase", "offset", "freq", "period" and "fitfunc"'''
    tt = numpy.array(tt)
    yy = numpy.array(yy)
    ff = numpy.fft.fftfreq(len(tt), (tt[1]-tt[0]))   # assume uniform spacing
    Fyy = abs(numpy.fft.fft(yy))
    guess_freq = abs(ff[numpy.argmax(Fyy[1:])+1])   # excluding the zero frequency "peak", which is related to offset
    guess_amp = numpy.std(yy) * 2.**0.5
    guess_offset = numpy.mean(yy)
    guess = numpy.array([guess_amp, 2.*numpy.pi*guess_freq, 0., guess_offset])

    def sinfunc(t, A, w, p, c):  return A * numpy.sin(w*t + p) + c
    popt, pcov = scipy.optimize.curve_fit(sinfunc, tt, yy, p0=guess)
    A, w, p, c = popt
    f = w/(2.*numpy.pi)
    fitfunc = lambda t: A * numpy.sin(w*t + p) + c
    return {"amp": A, "omega": w, "phase": p, "offset": c, "freq": f, "period": 1./f, "fitfunc": fitfunc, "maxcov": numpy.max(pcov), "rawres": (guess,popt,pcov)}

sin_param = fit_sin(X, y)


pred_file = open('bstar_pred.txt', 'w')
y_pred = []
for t in epoch:
	y_pred.append(sin_func(sin_param, t))
	pred_file.write(str(sin_func(sin_param, t)))
	pred_file.write('\n')
