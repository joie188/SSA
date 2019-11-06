import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


i = 53
r = 6928
GM = 3.986004418*math.pow(10,14)
period = 2*math.pi*math.sqrt(math.pow(r,3)/GM) #calculate period of initial satellite orbit

def calc_theta(elapsed_time):
    orbits = elapsed_time/period
    position = int(orbits)
    delta_position = orbits - position
    return 360/delta_position

def calc_coords(elapsed_time):
    theta = calc_theta(elapsed_time)
    x = r*math.sin(theta)
    y = r*math.cos(theta)*math.cos(i)
    z = r*math.cos(theta)*math.sin(i)
    return x, y, z

#print(period)
#print(calc_coords(10)) 