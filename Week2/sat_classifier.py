# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 21:10:06 2019

@author: Brian
"""

import numpy as np
import random
import pandas as pd
import string
        
def can_be_floated(array):
    for i in array:
        if isinstance(i, float) or isinstance(i, int):
            if np.isnan(i):
                continue
            return False
        for char in i:
            if char not in '1234567890,':
                return False
        return True
        
def floatify(array):
    new_array = []
    for i in array:
        if isinstance(i, str):
            try:
                i = float(i.translate(str.maketrans('', '', string.punctuation)))
            except ValueError:
                pass
        new_array.append(i)   
    return new_array


def all_same(array):
    same_type = type(array[0])
    for i in array:
        if type(i) != same_type:
            return False
    return True

def is_relevant(attr):
    result = 'Perigee' in attr or 'Apogee' in attr or 'Eccentricity' in attr or 'Inclination' in attr or 'Period' in attr
    return result

def read_data(data, depth):
    '''
    Parses through prepared data and outputs convenient data for Satellite class initialization
    '''
    for i in range(depth):
        yield (data['Name of Satellite, Alternate Names'][i] ,{key:data[key][i] for key in data if is_relevant(key)}, data['Class of Orbit'][i], data['Type of Orbit'][i])

class Satellite:
    def __init__(self, interest_param):
        self.name, self.orbit_param, self.orbit_class, self.orbit_type = interest_param

    def __repr__(self):
        return repr(self.name) + repr(self.orbit_class) + repr(self.orbit_type)


"""ABOVE ARE USEFUL FUNCTIONS"""


        
data = pd.read_csv("Week2_Problem2.csv")
org_data = {}

for i in data:
    if 'Unnamed' not in i and i != 'Comments' and 'Source' not in i:
        org_data[i] = [i for i in data[i]]

for attr in org_data:
    data_list = org_data[attr]
    if can_be_floated(data_list):
        org_data[attr] = floatify(data_list)
        
sat_list = []
  
for i in read_data(org_data, 2062):
    sat_list.append(Satellite(i))

    
if __name__=='__main__':
    pass
