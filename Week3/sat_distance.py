import math
import pandas as pd
import numpy as np
import sat_class as sat

THRESHOLD = 200000 # distance in meters
encounters = [] #list of encounter objects

def time_matcher(timelist1, timelist2):
    matching_times = []
    threshold = .1
    for i in range(len(timelist1)):
        for j in range(len(timelist2)):
            if timelist1[i][0] != timelist2[j][0]:
                continue
            else:
                if abs(timelist1[i][1] - timelist2[j][1]) < threshold:
                    matching_times.append((timelist1[i], i, timelist2[j], j))
    return matching_times
            
class TLE:

    def __init__(self, relevant_info, scn):
        self.a = relevant_info[0]  #semi major axis (in meters)
        self.e = relevant_info[1]   #Eccentricity
        self.M = relevant_info[3]   #mean anomaly
        self.raa = np.deg2rad(relevant_info[4]) #Right ascention of ascending node (Omega)
        self.periapsis = np.deg2rad(relevant_info[5])   #Argument of periapsis (omega)
        self.i = np.deg2rad(relevant_info[2])   #inclination

        self.scn = scn

    def calc_radius(self):

        r = (self.a*(1 - self.e**2))/(1 + self.e*np.cos(self.periapsis))
        return r

    def calc_coords(self):
        r = self.calc_radius()
        x = r*(np.cos(self.raa)*np.cos(self.periapsis + self.raa) - np.sin(self.raa)*np.sin(self.periapsis + self.raa)*np.cos(self.i))
        y = r*(np.cos(self.raa)*np.cos(self.periapsis + self.raa) - np.sin(self.raa)*np.sin(self.periapsis + self.raa)*np.cos(self.i))
        z = r*np.sin(self.periapsis + self.raa)*np.sin(self.i)
        coords = [x,y,z]
        return coords

def calc_distance(coords1, coords2):
        x1,y1,z1 = coords1
        x2,y2,z2 = coords2

        dist = math.sqrt( (x1-x2)**2 + (y1-y2)**2 + (z1+z2)**2)

        return dist

def compare_sats(file1, file2, distance):
    info1 = sat.vectorize(file1)
    info2 = sat.vectorize(file2)
    
    TLE1 = TLE(*info1[:2])
    TLE2 = TLE(*info2[:2])
    
    cart1 = TLE1.calc_coords()
    cart2 = TLE2.calc_coords()
    distances = []
    
    sat_info = {}
    # dict, keys are times where satellites are within close time frame, values are distances from each other
    coincide_times = time_matcher(info1[2], info2[2])
#    print(coincide_times)
    for pair in coincide_times:
        coord1 = (cart1[0][pair[1]], cart1[1][pair[1]], cart1[2][pair[1]])
        coord2 = (cart2[0][pair[3]], cart2[1][pair[3]], cart2[2][pair[3]])
        if calc_distance(coord1, coord2) < distance:
            sat_info[(pair[0], pair[2])] = calc_distance(coord1, coord2)
            
    return sat_info
    
def compare_all_sats(min_distance):
    datasets = ['25473.txt', '26824.txt', '27438.txt', '39509.txt', '40258.txt']
    comparisons = {i for i in [tuple(sorted([i,j])) for i in datasets for j in datasets] if i[0] != i[1]}
    close_approaches = []
    
    for pair in comparisons:
        close_approaches.append((pair, compare_sats(*pair, min_distance)))
        
    return close_approaches
        


#class TLE:
#
#    def __init__(self, relevant_info, scn, time):
#        self.a = relevant_info[0]  #semi major axis (in meters)
#        self.e = relevant_info[1]   #Eccentricity
#        self.M = relevant_info[3]   #mean anomaly
#        self.raa = relevant_info[4] #Right ascention of ascending node (Omega)
#        self.periapsis = relevant_info[5]   #Argument of periapsis (omega)
#        self.i = relevant_info[2]   #inclination
#
#        self.time = time
#        self.scn = scn
#
#    def calc_radius(self):
#
#        r = (self.a*(1 - math.pow(self.e,2)))/(1 + self.e*math.cos(self.periapsis))
#        return r
#
#    def calc_coords(self):
#        r = self.calc_radius()
#        x = r*(math.cos(self.raa)*math.cos(self.periapsis + self.raa) - math.sin(self.raa)*math.sin(self.periapsis + self.raa)*math.cos(self.i))
#        y = r*(math.cos(self.raa)*math.cos(self.periapsis + self.raa) - math.sin(self.raa)*math.sin(self.periapsis + self.raa)*math.cos(self.i))
#        z = r*math.sin(self.periapsis + self.raa)*math.sin(self.i)
#        coords = [x,y,z]
#        return coords
#
#    def calc_distance(self, sat):
#        coords = self.calc_coords()
#        x1 = coords[0]
#        y1 = coords[1]
#        z1 = coords[2]
#
#        sat_coords = sat.calc_coords()
#        x2 = sat_coords[0]
#        y2 = sat_coords[1]
#        z2 = sat_coords[2]
#
#
#        dist = math.sqrt( (x1-x2)**2 + (y1-y2)**2 + (z1+z2)**2)
#
#        return dist
#
#class encounter:
#
#    def __init__(self, distance, scn1, scn2, time):
#        self.distance = distance
#        self.scn1 = scn1
#        self.scn2 = scn2
#        self.time = time
#
#    def __str__(self):
#        return "distance at time " + str(self.time) + " between " + str(self.scn1) + ' and ' + str(self.scn2) + ' is ' + str(self.distance)
#
#
#def compare_sats(file1, file2, threshold):
#    print("comparing", file1, 'and', file2)
#
#    sats1 = [] # list for out1
#    sats2 = {} # time:tle for out2
#
#    out1 = sat.output(file1)
#    out2 = sat.output(file2)
#
#    for obj in out1:
#        tle1 = TLE(obj['relevant_info'], obj['scn'], obj['time'])
#        sats1.append(tle1)
#    for obj in out2:
#        tle2 = TLE(obj['relevant_info'], obj['scn'], obj['time'])
#        sats2[str(tle2.time[0]) + str(tle2.time[1])] = tle2
#
#    
#
#    for tle in sats1:
#        closest_time = sat.get_nearest_time(tle.time, file2, 1)
#        comparison_sat = sats2[str(int(closest_time[0])) + str(closest_time[1])]
#
#        distance = tle.calc_distance(comparison_sat)
#
#        if distance < threshold:
#            enc = encounter(distance, tle.scn, comparison_sat.scn, tle.time)
#            print(enc)
#            encounters.append(enc)
#
#    #import pdb; pdb.set_trace()
#
#if __name__ == '__main__':
#
#    datasets = ['25473.txt', '26824.txt', '27438.txt', '39509.txt', '40258.txt']
#    
#    
#    for i in range(len(datasets)):
#        for j in range(i+1, len(datasets) - 1):
#            compare_sats(datasets[i], datasets[j], THRESHOLD)
#
#    for enc in encounters:
#        print(enc)
#
#
#
#
#
#
#
#
#

