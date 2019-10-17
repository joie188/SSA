import math
import pandas as pd
import numpy as np
import sat_class as sat

THRESHOLD = 200000 # distance in meters
encounters = [] #list of encounter objects

class TLE:

    def __init__(self, relevant_info, scn, time):
        self.a = relevant_info[0]  #semi major axis (in meters)
        self.e = relevant_info[1]   #Eccentricity
        self.M = relevant_info[3]   #mean anomaly
        self.raa = relevant_info[4] #Right ascention of ascending node (Omega)
        self.periapsis = relevant_info[5]   #Argument of periapsis (omega)
        self.i = relevant_info[2]   #inclination

        self.time = time
        self.scn = scn

    def calc_radius(self):

        r = (self.a*(1 - math.pow(self.e,2)))/(1 + self.e*math.cos(self.periapsis))
        return r

    def calc_coords(self):
        r = self.calc_radius()
        x = r*(math.cos(self.raa)*math.cos(self.periapsis + self.raa) - math.sin(self.raa)*math.sin(self.periapsis + self.raa)*math.cos(self.i))
        y = r*(math.cos(self.raa)*math.cos(self.periapsis + self.raa) - math.sin(self.raa)*math.sin(self.periapsis + self.raa)*math.cos(self.i))
        z = r*math.sin(self.periapsis + self.raa)*math.sin(self.i)
        coords = [x,y,z]
        return coords

    def calc_distance(self, sat):
        coords = self.calc_coords()
        x1 = coords[0]
        y1 = coords[1]
        z1 = coords[2]

        sat_coords = sat.calc_coords()
        x2 = sat_coords[0]
        y2 = sat_coords[1]
        z2 = sat_coords[2]


        dist = math.sqrt( (x1-x2)**2 + (y1-y2)**2 + (z1+z2)**2)

        return dist

class encounter:

    def __init__(self, distance, scn1, scn2, time):
        self.distance = distance
        self.scn1 = scn1
        self.scn2 = scn2
        self.time = time

    def __str__(self):
        return "distance at time " + str(self.time) + " between " + str(self.scn1) + ' and ' + str(self.scn2) + ' is ' + str(self.distance)


def compare_sats(file1, file2, threshold):
    print("comparing", file1, 'and', file2)

    sats1 = [] # list for out1
    sats2 = {} # time:tle for out2

    out1 = sat.output(file1)
    out2 = sat.output(file2)

    for obj in out1:
        tle1 = TLE(obj['relevant_info'], obj['scn'], obj['time'])
        sats1.append(tle1)
    for obj in out2:
        tle2 = TLE(obj['relevant_info'], obj['scn'], obj['time'])
        sats2[str(tle2.time[0]) + str(tle2.time[1])] = tle2

    

    for obj in sats1:
        closest_time = sat.get_nearest_time(obj.time, file2, 1)
        comparison_sat = sats2[str(int(closest_time[0])) + str(closest_time[1])]

        distance = obj.calc_distance(comparison_sat)

        if distance < threshold:
            enc = encounter(distance, obj.scn, comparison_sat.scn, obj.time)
            print(enc)
            encounters.append(enc)

    #import pdb; pdb.set_trace()

if __name__ == '__main__':

    datasets = ['25473.txt', '26824.txt', '27438.txt', '39509.txt', '40258.txt']

    for i in range(0, len(datasets) - 1):
        for j in range(i+1, len(datasets)):
            compare_sats(datasets[i], datasets[j], THRESHOLD)

    for enc in encounters:
        print(enc)









