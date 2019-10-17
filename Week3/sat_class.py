# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:13:40 2019

@author: Brian
"""

import math
import numpy as np

CRIT_INCLINATION = 63.4
EARTH_RADIUS = 6371000 #in m
EARTH_MASS = 5167000000000.0
GRAV_PARAM = 398600441800000.0

MOLNIYA_ORBIT_A = 26600000 # meters
MOLNIYA_RANGE = 0.11


def output(text_file):
    f = open(text_file, 'r')
    satellite_parameters = []
    while True:
        line1 = f.readline().split()
        line2 = f.readline().split()
        if not line1 or not line2:
            break  #end of file
        sat_param = {}
        sat_param["scn"] = line1[1]     #Satellite catalog number
        e = "." + line2[4]
        relevant_info = [semimajor_axis(float(line2[7])), float(e), float(line2[2]), float(line2[6]), float(line2[3]), float(line2[5])]
                         #semi major axis (in meters)   Eccentricity    inclin        mean anomaly        Omega            omega             
        sat_param['orbit_params'] = classify_orbit(*relevant_info[:3]) # tuple containing orbit class, apogee, perigee
        sat_param['relevant_info'] = relevant_info
        sat_param['time'] = (int(line1[3][:2]), float(line1[3][2:])) # tuple containing year in  first position, day and fractional day in second
        satellite_parameters.append(sat_param)
    return satellite_parameters

def vectorize(text_file):
    data = output(text_file)
    # gets data from text file
    params = np.array([entry['relevant_info'] for entry in data]).transpose() # converts to column vector
    times = np.array([entry['time'] for entry in data])
    return (params, times)

def semimajor_axis(mean_motion):
    '''
    Calculates semimajor axis based on formula T (period) = 2pi*sqrt(a^3/grav_param)
    '''
    period = 86400*(1/mean_motion) # Converts to Hertz
    factor = 2*math.pi
    result = (GRAV_PARAM*(period/factor)**2)**(1/3)
    return round(result,4)

def classify_orbit(a, e, i):
    '''
    Classifies the orbit as either LEO, MEO, GEO, or HEO
    '''
    orbit_type = ''
    apo = a*(1 + e) - EARTH_RADIUS
    peri = a*(1 - e) - EARTH_RADIUS
    if a >= 41263000 and a <= 42166000: #technically perfectly geosynchronous orbits have a semi-major axis of 41,264 km
        orbit_type = "GEO"
    elif apo < 2000000 and peri < 2000000:
        orbit_type = "LEO"
    elif apo >= 2000000 and apo < 35786000: #and peri >= 2000000 and peri <= 35876000:
        orbit_type = "MEO"
    elif apo > 35786000: #and peri > 35786000:
        orbit_type = "HEO"
    
    return (orbit_type, apo, peri)
