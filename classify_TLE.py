import math

def output(text_file):
    f = open(text_file, 'r')
    while True:
        line1 = f.readline().split()
        line2 = f.readline().split()
        if not line1 or not line2: 
            break  #end of file
        print(line1) 
        print(line2)
        print("Satellite catalog number: ", line1[1])
        print("Semi-major axis (a): ", semimajor_axis(float(line2[7])))
        print("Eccentricity (e): ", line2[4])
        print("Mean anomaly (M): ", line2[6])
        print("Right ascention of ascending node (Ω): ", line2[3])
        print("Argument of periapsis (ω): ", line2[5])
        print("Inclination (i): ", line2[2])


output("TLE.txt")

def semimajor_axis(mean_motion):
    period = 86400*(1/mean_motion)
    grav_parameter = 398600441800000.0
    factor = 2*math.pi
    
    result = (grav_parameter*(period/factor)**2)**(1/3)
    return result