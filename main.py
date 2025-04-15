#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain = Brain()

# Robot configuration code
brain_inertial = Inertial()
optical_9 = Optical(Ports.PORT1)
distance_7 = Distance(Ports.PORT2)
motor_3 = Motor(Ports.PORT3, False)
motor_group_6_motor_a = Motor(Ports.PORT6, False)
motor_group_6_motor_b = Motor(Ports.PORT10, True)
motor_group_6 = MotorGroup(motor_group_6_motor_a, motor_group_6_motor_b)
bumper_a = Bumper(brain.three_wire_port.a)
bumper_b = Bumper(brain.three_wire_port.b)
motor_4 = Motor(Ports.PORT4, False)
distance_Down = Distance(Ports.PORT7)


# Wait for sensor(s) to fully initialize
wait(100, MSEC)

# generating and setting random seed
def initializeRandomSeed():
    wait(100, MSEC)
    xaxis = brain_inertial.acceleration(XAXIS) * 1000
    yaxis = brain_inertial.acceleration(YAXIS) * 1000
    zaxis = brain_inertial.acceleration(ZAXIS) * 1000
    systemTime = brain.timer.system() * 100
    urandom.seed(int(xaxis + yaxis + zaxis + systemTime)) 

# Initialize random seed 
initializeRandomSeed()

#endregion VEXcode Generated Robot Configuration
# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode EXP Python Project
# 
# ------------------------------------------

# Library imports
from vex import *





def findObject():
    #move until it finds and object on table
    count1 = 0
    while distance_7.object_distance(MM) > 1000:
        print(distance_7.object_distance(MM))
        if count1 == 100 or distance_7.object_distance(MM) < 300:
            go1 = True
            break
            
        motor_group_6_motor_a.spin_for(FORWARD,45,DEGREES)
        count1 += 1 

#initialise variables
go = True
motor_group_6.set_max_torque(100,PERCENT)
count = 0
ambientHue = optical_9.hue()
detectedHue = ambientHue + 5



#move until it finds and object on table

count1 = 0
while distance_7.object_distance(MM) > 1000:
    print(distance_7.object_distance(MM))
    if count1 == 1000 or distance_7.object_distance(MM) < 300:
        go1 = True
        break
            
    motor_group_6_motor_a.spin_for(FORWARD,45,DEGREES)
    count1 += 1
motor_group_6_motor_a.spin_for(FORWARD,20,DEGREES)


#move towards object
while go:
    print(distance_7.object_distance(MM))
    print(distance_Down.object_distance(MM))

    #if object is close stop moving
    if distance_Down.object_distance(MM) > 110:
        motor_group_6.spin_for(REVERSE, 720, DEGREES)
        motor_group_6_motor_a.spin_for(FORWARD,180,DEGREES)
        findObject()

    #if robot going off table stop
    elif distance_7.object_distance(MM) < 95:

        motor_4.spin_for(FORWARD,90,DEGREES)
        motor_3.spin_for(FORWARD,90,DEGREES)
        go = False
    #count how far forward robo has moved
    else:
        count += 1
        motor_group_6.spin_for(FORWARD,180,DEGREES)

#return to person 
while count > 0:
    motor_group_6.spin_for(REVERSE,180,DEGREES)
    count -= 1
motor_group_6_motor_a.spin_for(FORWARD,1080,DEGREES)
motor_4.spin_for(REVERSE,90,DEGREES)
#port 5 is dodgy

 
"""

while True:
            wait(2, SECONDS)


            print(ambientHue)
            print(optical_9.hue())
            if  optical_9.hue() > detectedHue:
                correctObject = True
                break
            break
        if correctObj == True:

"""
