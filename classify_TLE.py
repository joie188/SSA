import math

def output(text_file):
    f = open(text_file, 'r')
    satellite_parameters = []
    while True:
        line1 = f.readline().split()
        line2 = f.readline().split()
        if not line1 or not line2: 
            break  #end of file
        sat_param = {}
        sat_param["scn"] = line1[1]     #Satellite catalog number
        sat_param["a"] = semimajor_axis(float(line2[7]))   #semi major axis
        sat_param["e"] = float(line2[4])                    #Eccentricity 
        sat_param["M"] = float(line2[6])                    #mean anomaly
        sat_param["raa"] = float(line2[3])                  #Right ascention of ascending node (Ω)
        sat_param["periapsis"] = float(line2[5])            #Argument of periapsis (ω)
        sat_param["i"] = float(line2[2])                    #inclination
        satellite_parameters.append(sat_param)
    return satellite_parameters

def semimajor_axis(mean_motion):
    period = 86400*(1/mean_motion)
    grav_parameter = 398600441800000.0
    factor = 2*math.pi
    
    result = (grav_parameter*(period/factor)**2)**(1/3)
    return result

for sat in (output("TLE.txt")):
    print(sat)