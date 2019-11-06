import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import norm
#eph_data = pd.read_csv('ssa_urop_maneuver_10001.txt', header=None)
'''
def kf_predict(X, P, A, Q, B, U):
    X = np.dot(A, X) + np.dot(B, U)
    P = np.dot(A, np.dot(P, A.T)) + Q
    return(X,P) 

def kf_update(X, P, Y, H, R):
    IM = np.dot(H, X)
    IS = R + np.dot(H, np.dot(P, H.T))
    K = np.dot(P, np.dot(H.T, np.inv(IS)))
    X = X + np.dot(K, (Y-IM))
    P = P - np.dot(K, np.dot(IS, K.T))
    LH = gauss_pdf(Y, IM, IS)
    return (X,P,K,IM,IS,LH)

def gauss_pdf(X, M, S):
    if M.shape()[1] == 1:
        DX = X - tile(M, X.shape()[1])
        E = 0.5 * np.sum(DX * (np.dot(np.inv(S), DX)), axis=0)
        E = E + 0.5 * M.shape()[0] * log(2 * pi) + 0.5 * log(np.det(S))
        P = np.exp(-E)
    elif X.shape()[1] == 1:
        DX = tile(X, M.shape()[1])- M
        E = 0.5 * np.sum(DX * (np.dot(np.inv(S), DX)), axis=0)
        E = E + 0.5 * M.shape()[0] * log(2 * pi) + 0.5 * log(np.det(S))
        P = np.exp(-E)
    else:
        DX = X-M
        E = 0.5 * np.dot(DX.T, np.dot(np.inv(S), DX))
        E = E + 0.5 * M.shape()[0] * log(2 * pi) + 0.5 * log(np.det(S))
        P = np.exp(-E)
    return (P[0],E[0])

dt = 600 # Time Step between Filter Steps
X = np.matrix([0.0, 0.0, 1.0, 10.0, 0.0, 0.0, 0.0, 0.0, -9.81]).T #initial state (have to change)
P = 0.1*np.eye(9) #Initial Uncertainty
A = np.matrix([[1.0, 0.0, 0.0, dt, 0.0, 0.0, 0.5*dt**2, 0.0, 0.0],
              [0.0, 1.0, 0.0, 0.0,  dt, 0.0, 0.0, 0.5*dt**2, 0.0],
              [0.0, 0.0, 1.0, 0.0, 0.0,  dt, 0.0, 0.0, 0.5*dt**2],
              [0.0, 0.0, 0.0, 1.0, 0.0, 0.0,  dt, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0,  dt, 0.0],
              [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0,  dt],
              [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
              [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]])  #dynamic matrix
Q = np.eye(X.shape()[0])
B = np.eye(X.shape()[0]) 
U = np.zeros((X.shape()[0],1)) 
# Measurement matrices
Y = np.array([ [X[0,0]], [X[1,0]] ])
H = np.matrix([[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])
#Measurement Noise Covariance Matrix
rp = 1.0**2  # Noise of Position Measurement
R = np.matrix([[rp, 0.0, 0.0],
               [0.0, rp, 0.0],
               [0.0, 0.0, rp]])
# Number of iterations in Kalman Filter
N_iter = 50
# Applying the Kalman Filter
for i in arange(0, N_iter):
    (X, P) = kf_predict(X, P, A, Q, B, U)
    (X, P, K, IM, IS, LH) = kf_update(X, P, Y, H, R)
    Y = np.array([[X[0,0] + abs(0.1 * randn(1)[0])],[X[1, 0] + abs(0.1 * randn(1)[0])]]) '''

eph_data = pd.read_csv('ssa_urop_maneuver_10000.txt', header=None)
x = []
y = []
z = []
xv = []
yv = []
zv = []
t = []
time = 0
for row in eph_data[0]:
    r = row.split()
    t.append(time)
    time += 10
    x.append(float(r[7]))
    y.append(float(r[8]))
    z.append(float(r[9]))
    xv.append(float(r[10]))
    yv.append(float(r[11]))
    zv.append(float(r[12]))
#plt.plot(t, x, linestyle="",marker="o", color='g')
eph = pd.read_csv('ssa_urop_maneuver_10006.txt', header=None)
xx = []
yy = []
zz = []
xxv = []
yyv = []
zzv = []
for row in eph[0]:
    r = row.split()
    xx.append(float(r[7]))
    yy.append(float(r[8]))
    zz.append(float(r[9]))
    xxv.append(float(r[10]))
    yyv.append(float(r[11]))
    zzv.append(float(r[12]))
for i in range(len(x)):
    if abs (x[i] - xx[i]) > .1:
        print("xt", t[i])
        print(x[i])
        print(xx[i])
    if abs (y[i] - yy[i]) > .1:
        print("yt", t[i])
        print(y[i])
        print(yy[i])
    if abs (z[i] - zz[i]) > .1:
        print("zt", t[i])
    if abs (xv[i] - xxv[i]) > .1:
        print("xt", t[i])
        print(x[i])
        print(xx[i])
    if abs (yv[i] - yyv[i]) > .1:
        print("yt", t[i])
    if abs (zv[i] - zzv[i]) > .1:
        print("zt", t[i])
#plt.plot(t, x, linestyle="",marker="o", color='r')
#plt.show()