import math
import pandas as pd
import numpy as np
import sat_class as sat

sat1 = []
time1 = []
sat2 = []
time2 = []
a = 0.0
e = 0.0
M = 0.0
raa = 0.0
periapsis = 0.0
i = 0.0
x = 0.0
y = 0.0
z = 0.0

def orbital_parameters(txt1, txt2):
    sat1 = sat.vectorize(txt1)[0]
    sat2 = sat.vectorize(txt2)[0]
    return sat1, sat2

def calc_time(txt1, txt2):
    time1 = sat.vectorize(txt1)[1]
    time2 = sat.vectorize(txt2)[1]
    if(time1[1][0][1] < time2[1][0][1]):
        return time1
    else:
        temp_sat = sat1
        sat1 = sat2
        sat2 = temp_sat
        return time2

def set_parameters(sat_num,j):
    a = sat_num[0][j]          #semi major axis (in meters)
    e = sat_num[1][j]          #Eccentricity
    M = sat_num[2][j]          #mean anomaly
    raa = sat_num[3][j]        #Right ascention of ascending node (Omega)
    periapsis = sat_num[4][j]  #Argument of periapsis (omega)
    i = sat_num[5][j]          #inclination
    return a, e, M, raa, periapsis, i

def calc_coords(sat_num):
    r = (a*(1 - math.pow(e,2)))/(1 + e*math.cos(periapsis))
    x = r*(math.cos(raa)*math.cos(periapsis + raa) - math.sin(raa)*math.sin(periapsis + raa)*math.cos(i))
    y = r*(math.cos(raa)*math.cos(periapsis + raa) - math.sin(raa)*math.sin(periapsis + raa)*math.cos(i))
    z = r*math.sin(periapsis + raa)*math.sin(i)
    coords = [x,y,z]
    return coords

def calc_distance(coords1, coords2):
    dist = math.sqrt(math.pow(coords1[0],2), math.pow(coords1[1],2), math.pow(coords1[2],2))
    return dist

for j in range():
    sat1, sat2 = orbital_parameters("25473.txt", "26824.txt")
    desired_sat, shortest_time = calc_time("25473.txt", "26824.txt")
    tle = sat.get_nearest_time(desired_sat, shortest_time)
    print(tle)
    a, e, M, raa, periapsis, i = set_parameters(sat1,j)