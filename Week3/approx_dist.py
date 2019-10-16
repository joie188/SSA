import math
import pandas as pd
import numpy as np
import sat_class as sat

sat1 = []
time1 = []
sat2 = []
time2 = []

def orbital_parameters(txt1, txt2):
    sat1 = sat.vectorize("txt1")[0]
    sat2 = sat.vectorize("txt2")[0]

def calc_time():
    time1 = sat.vectorize("txt1")[1]
    time2 = sat.vectorize("txt2")[1]
    if(time1[1][0][1] < time2[1][0][1]):
        return time1
    else:
        return time2

satellite_parameters = sat.output("25473.txt")
print(satellite_parameters)
a = 0   #semi major axis (in meters)
e = 0   #Eccentricity
M = 0   #mean anomaly
raa = 0 #Right ascention of ascending node (Omega)
periapsis = 0   #Argument of periapsis (omega)
i = 0   #inclination

def calc_radius(sat_num):
    r = (a*(1 - math.pow(e,2)))/(1 + e*math.cos(periapsis))
    return r

def calc_coords(sat_num):
    r = calc_radius(sat_num)
    x = r*(math.cos(raa)*math.cos(periapsis + raa) - math.sin(raa)*math.sin(periapsis + raa)*math.cos(i))
    y = r*(math.cos(raa)*math.cos(periapsis + raa) - math.sin(raa)*math.sin(periapsis + raa)*math.cos(i))
    z = r*math.sin(periapsis + raa)*math.sin(i)
    coords = [x,y,z]
    return coords

def calc_distance():

