# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 02:51:53 2019

@author: luke
"""
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt
import time
#%%

def convertToTLETime(parsed_time):
    year = float(time.strftime('%y', parsed_time))
    day = float(time.strftime('%j', parsed_time))
    hour = float(time.strftime('%H', parsed_time))
    minute = float(time.strftime('%M', parsed_time))
    
    day_fraction = (hour + (minute / 60.0)) / 24.0
    
    tle_time = year * 1000 + day + day_fraction
    
    return format(tle_time, '.8f')

def gather_data(file, pattern_type):
    data = pd.read_csv(file)
    current_id = 0
    sat_dict = {}
    epoch_time = []
    
    for i in range(len(data)):
        row = data.iloc[i]
        if pattern_type == 1:
            pattern = '%Y-%m-%d %H:%M:%S'
        else:
            pattern = '%m/%d/%Y %H:%M'
        
#        norm_time = int(time.mktime(time.strptime(row["EPOCH"], pattern)))
#        epoch_time.append(norm_time)
        # tle time
        epoch_time.append(convertToTLETime(time.strptime(row["EPOCH"], pattern)))
    
    data['TIME'] = epoch_time

    for i in range(len(data)):
        row = data.iloc[i]
        if row["NORAD_CAT_ID"] != current_id:
            current_id = row['NORAD_CAT_ID']
            sat_dict[current_id] = data.loc[data.NORAD_CAT_ID == current_id]
            
    return sat_dict
#%%
week1 = gather_data("AstroYWeek1DataSet.csv",  0)
week2 = gather_data("AstroYWeek2DataSet.csv",  1)
week3 = gather_data("AstroYWeek3DataSet.csv", 0)
week4 = gather_data("AstroYWeek4DataSet.csv", 1)
tasking = gather_data("USSTRATCOM_TASKING_REQUEST_Group2.csv", 1)


datasets = [week1, week2, week3, week4, tasking]
#%%

sats = [74415, 9191, 11682, 30206,
        79815, 10814, 12605, 54494,
        55340, 58006, 75276, 87343,
        88756, 9356, 31859, 36829,
        45268, 47507, 70237, 72643,
        74562, 74866, 87337, 89581, 95609]

#sats = [10814]
for id in sats:
    tlefile = open("tles/{}.txt".format(id), 'w')
    for set in datasets:
        
        if id not in set:
            continue
        
        sat = set[id]
        
        for i in range(len(sat)):
            row = sat.iloc[i]
            line1 = "1 " + str(row['NORAD_CAT_ID']) + "U" + "          " + str(row['TIME']) + "  .00000000  00000-0  00000-0 0 00000\n"
            line2 = "2 " + str(row['NORAD_CAT_ID']) + " "
            
            inc = format(row["INCLINATION"], '.4f')
            line2 += inc.rjust(8, '0') + " "
                            
            raan = row["RA_OF_ASC_NODE"]
            str_raan = format(raan, '.4f')
            
            line2 += str_raan.rjust(7, '0') + " "
            
            ecc = str(int(row["ECCENTRICITY"] * 10000000))
            line2 += ecc.rjust(7,'0') + " "
            
            aop = format(row['ARG_OF_PERICENTER'], '0.4f')
            line2 += aop.rjust(8, '0') + " "
            
            ma = format(row['MEAN_ANOMALY'], '0.4f')
            line2 += ma.rjust(8, '0') + " "
            
            mm = format(row['MEAN_MOTION'],'.14f')
            line2 += mm.rjust(17, '0')+ "\n"
            
            tlefile.write(line1)
            tlefile.write(line2)
            
            print(line1)
            print(line2)
            
    tlefile.close()
    
