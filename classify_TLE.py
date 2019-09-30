import math
from astropy.table import Table
import numpy as np

CRIT_INCLINATION = 63.4
EARTH_MASS = 5167000000000.0
GRAV_PARAM = 398600441800000.0

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
        sat_param["a"] = semimajor_axis(float(line2[7]))   #semi major axis
        e = "." + line2[4]
        sat_param["e"] = float(e)                           #Eccentricity 
        sat_param["M"] = float(line2[6])                    #mean anomaly
        sat_param["raa"] = float(line2[3])                  #Right ascention of ascending node (Omega)
        sat_param["periapsis"] = float(line2[5])            #Argument of periapsis (omega)
        sat_param["i"] = float(line2[2])                    #inclination
        satellite_parameters.append(sat_param)
    return satellite_parameters

def semimajor_axis(mean_motion):
    '''
    Calculates semimajor axis based on formula T (period) = 2pi*sqrt(a^3/grav_param)
    '''
    period = 86400*(1/mean_motion) # Converts to Hertz
    factor = 2*math.pi
    result = (GRAV_PARAM*(period/factor)**2)**(1/3)
    return result

def circular_orbit(e):
    if e >= 0.5:
        return "elliptical orbit"
    elif e >= 0.01:
        return "near-circular orbit"
    elif e >= 0:  
        return "circular orbit"

def is_sun_synchronous(i, a):
    '''
    Returns if the satellite is sun-synchronous (only for near-circular orbits)
    '''
    T = 2 * math.pi * (a**3/EARTH_MASS)**0.5            #orbital period 
    if abs(math.cos(i) - (T/3.795)**(7/3)) <= .001:
        return "sun-synchronous"
    else:
        return "not sun-synchronous"

def is_critically_inclined(i):
    return abs(i - CRIT_INCLINATION) <= 0.5

for sat in (output("TLE.txt")):
    print(sat)                                                  #parameters from TLE file
    print(circular_orbit(sat['e']))                             #satellite's orbit
    if circular_orbit(sat['e']) == 'near-circular orbit':
        print(is_sun_synchronous(sat['i'], sat['a']))           #if near-circular, is sun-synchronous?
    if is_critically_inclined(sat['i']):                        #if critically inclined
        print("critically inclined orbit")
        
data = output("TLE.txt")        
t = Table(rows=data) 
print(t)
