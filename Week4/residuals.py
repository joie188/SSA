# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:45:22 2019

@author: Brian
"""

import numpy as np
import matplotlib.pyplot as plt
import math

mu = 398600441800000

def output(text_file):
    f = open(text_file, 'r')
    dates = []
    parameters = [[],[],[],[],[],[]]
    while True:
        line = f.readline().split()
        if not line:
            break
        line = [float(elem) for elem in line]
        time = line[1:7]
        a = line[7:13]
        for i in range(6):
            parameters[i].append(a[i])
        dates.append(time)

    return [dates, np.array(parameters)]

def compare_sats(sat_number):
    sat = 'ssa_urop_maneuver_1000{}.txt'.format(str(sat_number))
    sat_data = output(sat)
    control = output('ssa_urop_maneuver_10000.txt')
    
    diff = sat_data[1] - control[1]
    
    return diff

def mag(vector):
    return math.sqrt(sum([comp**2 for comp in vector]))

def coord_converter(x,y,z,vx,vy,vz):
    r = np.array([x,y,z])
    v = np.array([vx,vy,vz])
    
    speed = mag(v)
    dist = mag(r)
    
    h = np.cross(r,v)
    node = np.cross([0,0,1], h)
    e = np.cross((1/mu)*v, h)-(1/dist)*r
    
    E = 5.*(speed**2) - mu/dist
    
    semi_major = -mu/(2*E)
    
    inclin = (180/math.pi)*np.arccos(np.dot(h, [0,0,1])/mag(h))
    
    Omega = (180/math.pi)*np.arccos(np.dot([1,0,0], node)/mag(node))
    Omega = Omega if np.dot([0,1,0], node) >= 0 else 360 - Omega
    
    omega = (180/math.pi)*np.arccos(np.dot(node, e)/(mag(e)*mag(node)))
    omega = omega if np.dot([0,0,1], e) >= 0 else 360 - omega
    
    return (semi_major, mag(e), Omega, omega, inclin, E)


for i in range(1,7):
    print('Orbital profile for satellite ' + str(i))
    fig = plt.figure()
    sat = compare_sats(i)
    plt.plot([j for j in range(1441)], sat[0], linestyle="",marker=".")
    plt.show()
