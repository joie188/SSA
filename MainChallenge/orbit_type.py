#polar, deeply highly eccentric, sun-synchronous, non-polar inclined, equatorial

import math
import sys
import numpy as np
CRIT_INCLINATION = 63.4
EARTH_RADIUS = 6371000 #in m
EARTH_MASS = 5167000000000.0
GRAV_PARAM = 398600441800000.0

def polar(i):
    '''close to 90 degrees inclination'''
    return abs(i - 90) <= 1

def deeply_highly_eccentric(e):
    '''eccentricity close to but always less than 1'''
    if e >= 1:
        return False 
    return (1-e) <= 0.1

def sun_synchronous(i, sma):
    i = np.deg2rad(i)
    T = 2 * math.pi * (sma**3/EARTH_MASS)**0.5            #orbital period
    if abs(math.cos(math.radians(i)) - (T/3.795)**(7/3)) <= .001:
        return True
    else:
        return False

def non_polar_inclined(e, i):
    '''not too high eccentricity, inclination != 0 and != 90'''
    if abs(i) <= 0.1 or abs(i-90) <= 1:
        return False 
    return (e <= 0.75)

def equatorial(i):
    '''inclination near 0'''
    return abs(i) <= 1

def classify_orbit(sma, e, i):
    ''' Classifies the orbit as either LEO, MEO, GEO, or HEO '''
    apo = sma*(1 + e) - EARTH_RADIUS
    peri = sma*(1 - e) - EARTH_RADIUS
    if sma >= 41263000 and sma <= 42166000: #technically perfectly geosynchronous orbits have a semi-major axis of 41,264 km
        if i >= -0.1 and i <= 0.1:
            return "geostationary orbit"
        else:
            return "geosynchronous orbit (GEO)"
    elif apo < 2000000 and peri < 2000000:
        return "low earth orbit (LEO)"
    elif apo >= 2000000 and apo < 35786000: #and peri >= 2000000 and peri <= 35876000:
        return "medium earth orbit (MEO)"
    elif apo > 35786000: #and peri > 35786000:
        return "high earth orbit (HEO)"

if __name__=='__main__':
    #9356 i, e, sma = 97.646, 0.002154, 6858.69424899999    
    #74562 i, e, sma = 97.7029999999999, 0.000852999999999999, 6929.183443
    #75276 i, e, sma = 97.636, 0, 6939.130783
    #58006 i, e, sma = 97.755, 0.00155, 7027.202156
    #74415 i, e, sma = 97.731, 0.01388, 6546.723326
    #30206 i, e, sma = 97.729, 0.002783, 6928.853737
    print("Orbit: ", classify_orbit(sma, e, i))
    print("Polar: ", polar(i))
    print("DHE: ", deeply_highly_eccentric(e))
    print("SS: ", sun_synchronous(i, sma))
    print("NonPI: ", non_polar_inclined(e, i))
    print("Equa: ", equatorial(i))