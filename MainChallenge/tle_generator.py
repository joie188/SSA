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
    #print(format(tle_time, '.8f'))
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
        
        if row["MEAN_MOTION"] < 1:
            #import pdb; pdb.set_trace()

            data.at[i, "MEAN_MOTION"] *= 240.0
            row = data.iloc[i]
    
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
#datasets = [week1]
#%%

sats = [68, 5855, 6916, 8333, 8740, 9140, 9191, 9356, 9594, 10814, 
        10970, 11349, 11682, 12309, 12605, 15228, 15632, 15956, 
        16204, 16224, 16314, 16617, 18742, 21061, 24468, 24863, 
        26864, 27643, 28692, 30000, 30206, 31859, 33499, 33960, 
        34077, 36829, 37538, 38025, 38967, 39591, 44093, 44896,
        45105, 45268, 45935, 46729, 47507, 49231, 50450, 52822, 
        53207, 54494, 55041, 55340, 57872, 58006, 59114, 60283, 
        63646, 65215, 65817, 68564, 69128, 70082, 70237, 70502, 
        71823, 71909, 72643, 74415, 74562, 74796, 74866, 74906, 
        75276, 76684, 79359, 79606, 79712, 79815, 79991, 81683, 
        83471, 86077, 86116, 86892, 87168, 87337, 87343, 88150, 
        88756, 88819, 88854, 89581, 93428, 93836, 95609, 95991, 
        96484, 96564, 99277]

missing_sats = [74415, 9191, 11682, 30206,
        79815, 10814, 12605, 54494,
        55340, 58006, 75276, 87343,
        88756, 9356, 31859, 36829,
        45268, 47507, 70237, 72643,
        74562, 74866, 87337, 89581, 95609]

#sats = [10814]
for id in missing_sats:
    tlefile = open("missing_tles/{}.txt".format(id), 'w')
    for set in datasets:
        
        if id not in set:
            continue
        
        sat = set[id]
        
        for i in range(len(sat)):
            row = sat.iloc[i]
            line1 = "1 " + str(row['NORAD_CAT_ID']).rjust(5, '0') + "U" + "          " + str(row['TIME']) + "  .00000000  00000-0  00000-0 0 00000\n"
            line2 = "2 " + str(row['NORAD_CAT_ID']).rjust(5,'0') + " "
            
            inc = format(row["INCLINATION"], '.4f')
            line2 += inc.rjust(8, '0') + " "
                            
            raan = row["RA_OF_ASC_NODE"]
            str_raan = format(raan, '.3f')
            
            line2 += str_raan.rjust(7, '0') + "  "
            
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
            
#            print(line1)
#            print(line2)
            
    tlefile.close()
    
