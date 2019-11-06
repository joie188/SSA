'''import numpy as np
import pandas as pd

class KalmanFilter(object):
    def __init__(self, F=None, B=None, H=None, Q=None, R=None, P=None, x0=None):
        self.n = F.shape[1]
        self.m = H.shape[1]

        self.F = F
        self.H = H
        self.B = 0 if B is None else B
        self.Q = np.eye(self.n) if Q is None else Q
        self.R = np.eye(self.n) if R is None else R
        self.P = 100*np.eye(self.n) if P is None else P
        self.x = np.zeros((self.n, 1)) if x0 is None else x0

    def predict(self, u=0):
        self.x = np.dot(self.F, self.x) + np.dot(self.B, u)
        self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.Q
        return self.x

    def update(self, z):
        y = z - np.dot(self.H, self.x)
        S = self.R + np.dot(self.H, np.dot(self.P, self.H.T))
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
        self.x = self.x + np.dot(K, y)
        I = np.eye(self.n)
        self.P = np.dot(np.dot(I - np.dot(K, self.H), self.P),
                        (I - np.dot(K, self.H)).T) + np.dot(np.dot(K, self.R), K.T)


def example():
        dt = 600
        F = np.array([[1.0, 0.0, 0.0, dt, 0.0, 0.0, 0.5*dt**2, 0.0, 0.0],
              [0.0, 1.0, 0.0, 0.0,  dt, 0.0, 0.0, 0.5*dt**2, 0.0],
              [0.0, 0.0, 1.0, 0.0, 0.0,  dt, 0.0, 0.0, 0.5*dt**2],
              [0.0, 0.0, 0.0, 1.0, 0.0, 0.0,  dt, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0,  dt, 0.0],
              [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0,  dt],
              [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
              [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]])
        H = np.array([[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])
        Q = np.eye(9)
        R = np.eye(3)

        # x = np.linspace(-10, 10, 100)
        # measurements = - (x**2 + 2*x - 2)  + np.random.normal(0, 2, 100)
        eph_data = pd.read_csv('ssa_urop_maneuver_10000.txt', header=None)
        x0 = eph_data[0][0].split()
        x0 = x0[7:] + [0,0,0]
        x0 = [float(x) for x in x0]
        x0 = np.array([x0]).T
        measurements = []
        for row in eph_data[0]:
            r = row.split()
            measurements.append( [float(r[7]), float(r[8]), float(r[9])] )

        kf = KalmanFilter(F = F, H = H, Q = Q, R = R, x0=x0)
        predictions = []

        for z in measurements:
            pred = list(np.dot(H, kf.predict())[0])
            #print(pred)
            if len(pred) == 1:
                pred = [pred[0],0,0]
            predictions.append(pred)
            kf.update(z)

        import matplotlib.pyplot as plt
        plt.plot(range(len(measurements)), measurements, label = 'Measurements')
        plt.plot(range(len(predictions)), predictions, label = 'Kalman Filter Prediction')
        plt.legend()
        plt.show()

if __name__ == '__main__':
    example()
'''
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
eph_data = pd.read_csv('ssa_urop_maneuver_10001.txt', header=None)
time = []
data = []
t = 0
for row in eph_data[0]:
    r = row.split()
    time.append(t)
    t += 1
    data.append( (float(r[7])**2 + float(r[8])**2 + float(r[9])**2) ** 0.5 )
plt.plot(time, data, linestyle="",marker="o")
plt.show()
'''fig = pyplot.figure()
ax = Axes3D(fig)
x, y, z = [], [], []
for row in eph_data[0]:
    r = row.split()
    x.append( float(r[7]) )
    y.append( float(r[8]) )
    z.append( float(r[9]) )
ax.scatter(x, y, z)
pyplot.show()'''