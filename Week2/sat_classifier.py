# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 21:10:06 2019

@author: Brian
"""

import numpy as np
import random
import pandas as pd
import string
        
data = pd.read_csv("Week2_Problem2.csv")

org_data = {}

for i in data:
    if 'Unnamed' not in i and i != 'Comments' and 'Source' not in i:
        org_data[i] = [i for i in data[i]]

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

for attr in org_data:
    data_list = org_data[attr]
    if can_be_floated(data_list):
        org_data[attr] = floatify(data_list)
        
def all_same(array):
    same_type = type(array[0])
    for i in array:
        if type(i) != same_type:
            return False
    return True

for attr in org_data:
    print(attr, type(org_data[attr][0]), all_same(org_data[attr]))
    print('--------------------')