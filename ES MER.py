import numpy as np

configuration = input("What is the Configuration for your Exploration System? \n 1. Wheeled Rover \n 2. Tracked Rover \n 3. Walker System \n 4. Hopper \n 5. Slider \n 6. Aerial \n");
if configuration == "1":
    print("Rover is Wheeled Rover")
elif configuration == "2":
    print("Rover is Tracked Rover")        
elif configuration == "3":
    print("Rover is Walker System")
elif configuration == "4": 
    print("Rover is Hopper")
elif configuration == "5":
    print("Rover is Slider")
elif configuration == "6":
    print("Rover is an Aerial System")
    
PayloadMass = input("Estimated Payload Mass (kg): ")
MissionDuration = input("Expected mission duration (days): ") 
Body = input("To what planetary body will the mission go to? \n 1. Moon \n 2. Mars \n ")
if Body == "1":
    print("Mission will be going to the Moon")
elif Body == "2":
    print("Mission will be going to Mars")

MassPercentages = np.array([[0.0776, 0.0296, 0.0695, 0.1043, 0.0465, 0.0158, 0.2360, 0.2555, 0.0476, 0.1176], #Wheeled Rover (Real)
                            [0.0862, 0.1585, 0.1220, 0.0305, 0.0107, 0.0790, 0.2864, 0.0837, 0.0711, 0.0719], #Tracked
                            [0.1286, 0.1143, 0.1102, 0.0642, 0.1431, 0.0176, 0.0285, 0.1650, 0.1220, 0.1065], #Walker
                            [0.1912, 0.134 , 0.0605, 0.0453, 0.1194, 0.0206, 0.1256, 0.1024, 0.1128, 0.0883], #Hopper
                            [0.0887, 0.1269, 0.1496, 0.0662, 0.1149, 0.0863, 0.1321, 0.0857, 0.1414, 0.0082], #Slider
                            [0.1728, 0.1732, 0.1483, 0.0305, 0.0750, 0.0832, 0.1853, 0.0247, 0.0975, 0.0095]])#Aerial

def CalculateMasses(config, payload):
    TotalMass = float(payload)/float(MassPercentages[int(config)-1][9])
    
    MassPerSS = [0,0,0,0,0,0,0,0,0,0]
    i = 0
    #addition = 0
    
    for i in range(0, 10):
        MassPerSS[i] = float(MassPercentages[int(config)-1][i]) * TotalMass
        print("\n Mass of SS " + str(i+1) + " will be of " + str(round(MassPerSS[i], 2)) + "kg.")
        #addition = addition + MassPerSS[i]
        
    print("\n The ES total mass will be of " + str(round(TotalMass,2)) + "kg.")
    #print(addition)
    return 


CalculateMasses(configuration, PayloadMass);