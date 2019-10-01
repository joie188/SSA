import math
from astropy.table import Table
import numpy as np
import sys

CRIT_INCLINATION = 63.4
EARTH_RADIUS = 6371000 #in m
EARTH_MASS = 5167000000000.0
GRAV_PARAM = 398600441800000.0

MOLNIYA_ORBIT_A = 26600000 # meters
MOLNIYA_RANGE = 500000 # meters


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
        sat_param["a"] = semimajor_axis(float(line2[7]))   #semi major axis (in meters)
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
    return round(result,4)

def classify_orbit(a, e, i):
    '''
    Classifies the orbit as either LEO, MEO, GEO, or HEO
    '''
    apo = a*(1 + e) - EARTH_RADIUS
    peri = a*(1 - e) - EARTH_RADIUS
    if apo < 2000000 and peri < 2000000:
        return "low earth orbit (LEO)"
    elif apo >= 2000000 and apo < 35786000 and peri >= 2000000 and peri <= 35876000:
        return "medium earth orbit (MEO)"
    elif apo >= 35786000 and apo < 35787000 and peri >= 35786000 and peri < 35787000:
        if(i == 0):
            return "geostationary orbit"
        else:
            return "geosynchronous orbit (GEO)"
    elif apo > 35786000 and peri > 35786000:
        return "high earth orbit (HEO)"

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
    i = np.deg2rad(i)
    T = 2 * math.pi * (a**3/EARTH_MASS)**0.5            #orbital period 
    if abs(math.cos(i) - (T/3.795)**(7/3)) <= .001:
        return "sun-synchronous"
    else:
        return "not sun-synchronous"

def is_critically_inclined(i):
    return abs(i - CRIT_INCLINATION) <= 5


def is_molniya(sat):

    return abs(sat['periapsis'] - 270) <= 20 and is_critically_inclined(sat['i']) and abs(sat['a'] - MOLNIYA_ORBIT_A) <= MOLNIYA_RANGE

if __name__=='__main__':

    filname = ""
    if (len(sys.argv) != 2):
        filename = "TLE.txt"
    else:
        filename = sys.argv[1]

    for sat in (output(filename)):
        print(sat)                                                  #parameters from TLE file
        print(circular_orbit(sat['e']))                             #satellite's orbit
        
        if circular_orbit(sat['e']) == 'near-circular orbit':
            print(is_sun_synchronous(sat['i'], sat['a']))           #if near-circular, is sun-synchronous?

        if is_critically_inclined(sat['i']):                        #if critically inclined
            print("critically inclined orbit")

        if is_molniya(sat):
            print("molniya orbit")

        print('\n')
            
#    bigdata, smalldata = (output("geo_tle.txt"), output("TLE.txt"))   
#    t1 = Table(bigdata)
#    t2 = Table(smalldata) 
#    
#    print('Big dataset')
#    print(t1)
#    print('------------------------------------------')
#    print('Small dataset')
#    print(t2)

