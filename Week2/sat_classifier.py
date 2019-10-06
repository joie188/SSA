# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 21:10:06 2019

@author: Brian
"""

import numpy as np
import pandas as pd
import string
        
def can_be_floated(array):
    '''
    returns a boolean determining whether or not elements of an array need
    to be turned into float values
    '''
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
    '''
    Turns all values of an array into a float
    '''
    new_array = []
    for i in array:
        if isinstance(i, str):
            try:
                i = float(i.translate(str.maketrans('', '', string.punctuation)))
            except ValueError:
                pass
        new_array.append(i)   
    return new_array

def is_relevant(attr):
    result = 'Perigee' in attr or 'Apogee' in attr or 'Eccentricity' in attr or 'Inclination' in attr or 'Period' in attr
    return result

def read_data(data, depth):
    '''
    Parses through prepared data and outputs convenient data for Satellite class initialization
    '''
    for i in range(depth):
        yield (data['Name of Satellite, Alternate Names'][i], {key:data[key][i] for key in data if is_relevant(key)}, data['Class of Orbit'][i], data['Type of Orbit'][i])

class Satellite:
    def __init__(self, interest_param):
        """
        interest_param is a tuple containing a dict containing the satellite name,
        orbit parameters, and orbit classifications
        """
        self.name, self.orbit_param, self.orbit_class, self.orbit_type = interest_param
                  # dict containing     NEO, MEO, GEO,
                  # apogee, perigee,    or elliptical
                  # inclination, period,
                  # and eccentricity
                  
    def __repr__(self):
        return repr(self.name) + ', ' + repr(self.orbit_class) + repr(self.orbit_type)


"""ABOVE ARE USEFUL FUNCTIONS AND CLASSES"""



    
if __name__=='__main__':
    data = pd.read_csv("Week2_Problem2.csv")
    org_data = {}
    
    for attr in data:
        data_list = data[attr]
        if 'Unnamed' not in attr and attr != 'Comments' and 'Source' not in attr:
            if can_be_floated(data_list):
                org_data[attr] = floatify(data_list)
            else:
                org_data[attr] = [i for i in data_list]
            
    sat_list = [Satellite(i) for i in read_data(org_data, 2062)]
