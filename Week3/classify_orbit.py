import math
from astropy.table import Table
import numpy as np
import sys

CRIT_INCLINATION = 63.4
EARTH_RADIUS = 6371000 #in m
EARTH_MASS = 5167000000000.0
GRAV_PARAM = 398600441800000.0

MOLNIYA_ORBIT_A = 26600000 # meters
MOLNIYA_RANGE = 0.11

def output(text_file):
    f = open(text_file, 'r')
    satellite_parameters = []
    #'Perigee' 'Apogee''Eccentricity''Inclination''Period'
    while True:
        line1 = f.readline().split()
        line2 = f.readline().split()
        if not line2:
            break
        sat_param = {}
        
        a = semimajor_axis(float(line2[7])) 
        e = float("." + line2[4])
        sat_param["eccentricity"] = e                #Eccentricity

        apo = a*(1 + e) - EARTH_RADIUS
        peri = a*(1 - e) - EARTH_RADIUS
        sat_param['perigee'] = peri 
        sat_param['apogee'] = apo
        
        sat_param["inclination"] = float(line2[2])          #Inclination
        sat_param["period"] = 86400 * 1/(float(line2[7]))   #Period 
        satellite_parameters.append(sat_param)
         
    return satellite_parameters

def semimajor_axis(mean_motion):
    period = 86400*(1/mean_motion) # Converts to Hertz
    factor = 2*math.pi
    result = (GRAV_PARAM*(period/factor)**2)**(1/3)
    return round(result,4)

if __name__=='__main__':
    satellites = [25473, 26824, 27438, 39509, 40258]
    out = []
    for s in satellites:
        out.append(output(str(s)+".txt"))
    put_into_classifier = []
    for thing in out:
        thing = thing[0]
        put_into_classifier.append([thing['perigee'], thing['apogee'], thing['eccentricity'], thing['inclination'], thing['period']])
    print(put_into_classifier)