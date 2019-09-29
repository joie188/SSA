import math

def output(text_file):
    f = open(text_file, 'r')
    satellite_parameters = []
    while True:
        line1 = f.readline().split()
        line2 = f.readline().split()
        if not line1 or not line2: 
            break  #end of file
        print(line1) 
        print(line2)
        sat_param = []
        print("Satellite catalog number: ", line1[1])
        sat_param.append(line1[1])
        print("Semi-major axis (a): ", semimajor_axis(float(line2[7])))
        sat_param.append(semimajor_axis(float(line2[7])))
        print("Eccentricity (e): ", line2[4])
        sat_param.append(float(line2[4]))
        print("Mean anomaly (M): ", line2[6])
        sat_param.append(float(line2[6]))
        print("Right ascention of ascending node (Ω): ", line2[3])
        sat_param.append(float(line2[3]))
        print("Argument of periapsis (ω): ", line2[5])
        sat_param.append(float(line2[5]))
        print("Inclination (i): ", line2[2])
        sat_param.append(float(line2[2]))
        satellite_parameters.append(sat_param)
    print(satellite_parameters)
    
def semimajor_axis(mean_motion):
    # Calculates semimajor axis based on formula T (period) = 2pi*sqrt(a^3/grav_param)
    period = 86400*(1/mean_motion) # Converts to Hertz
    grav_param = 398600441800000.0 # Earth's mass * grav_constant
    factor = 2*math.pi
    
    result = (grav_param*(period/factor)**2)**(1/3)
    return result


output("TLE.txt")