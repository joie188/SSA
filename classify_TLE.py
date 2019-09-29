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
        #print("Semi-major axis (a): ", entry[1])
        print("Eccentricity (e): ", line2[4])
        print("Mean anomaly (M): ", line2[6])
        print("Right ascention of ascending node (Ω): ", line2[3])
        print("Argument of periapsis (ω): ", line2[5])
        print("Inclination (i): ", line2[2])


output("TLE.txt")