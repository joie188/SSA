# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:45:22 2019

@author: Brian
"""

import numpy as np

def output(text_file):
    f = open(text_file, 'r')
    parameters = []
    while True:
        line = f.readline().split()
        if not line:
            break
        line = [float(elem) for elem in line]
        name = int(line[0])
        time = line[1:7]
        r = line[7:10]
        v = line[10:13]
        parameters.append((name, time, r, v))

    return parameters
