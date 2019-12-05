#polar, deeply highly eccentric, sun-synchronous, non-polar inclined, equatorial

import math
import sys

CRIT_INCLINATION = 63.4
EARTH_RADIUS = 6371000 #in m
EARTH_MASS = 5167000000000.0
GRAV_PARAM = 398600441800000.0

MOLNIYA_ORBIT_A = 26600000 # meters
MOLNIYA_RANGE = 0.11

def polar(i):
    '''close to 90 degrees inclination'''
    pass 

def deeply_highly_eccentric(e):
    '''eccentricity close to but always less than 1'''
    if e >= 1:
        return False 
    return (1-e) <= 0.1

def sun_synchronous(i, a):
    i = np.deg2rad(i)
    T = 2 * math.pi * (a**3/EARTH_MASS)**0.5            #orbital period
    if abs(math.cos(math.radians(i)) - (T/3.795)**(7/3)) <= .001:
        return True
    else:
        return False

def non_polar_inclined():
    '''not too high eccentricity, inclination != 0 and != 90'''
    pass 

def equatorial():
    '''inclination near 0'''
    pass 