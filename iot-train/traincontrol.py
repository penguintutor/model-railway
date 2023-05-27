#!/usr/bin/python3
from gpiozero import Motor, Button
from time import sleep


# GPIO Pins (physical)
# Train 0 = 17,18 (11,12)
# Train 1 = 22,23 (15,16)
# Reed 0 = 4 (7)
# Reed 1 = 3 (5)


# list of motor pins [fwd, rev]
MOTORS = [
    [17, 18],
    [22, 23]
]

# Reed switches single list of switches which can be associated with any motor
REEDS = [4,3]

# max speed to reduce top speed
# maximum value is 1
MAX_SPEED = 1.0
# How long to wait between speed increases
ACC_DELAY = 0.5
# How long to wait at the station
STATION_DELAY = 10


# Setup motor objects
motors = []
for this_motor in MOTORS:
    motors.append(Motor (this_motor[0], this_motor[1]))

# Setup reed switch objects
reed_switches = []
for this_reed in REEDS:
    reed_switches.append (Button(this_reed))

#m1 = Motor (MOTOR_PIN_FWD, MOTOR_PIN_REV)
#reed_switch = Button (REED_PIN)

# Go from stop to max speed
def train_speed_up (max_speed, train=0):
    speed = 0
    while speed < max_speed:
        speed += 0.1
        if speed >= 1:
            speed = 1
        motors[train].forward(speed)
        sleep(ACC_DELAY)

def train_slow_down (current_speed, train=0):
    speed = current_speed
    while speed > 0:
        speed -= 0.1
        if speed <= 0 :
            motors[train].stop()
        else:
            motors[train].forward(speed)
        sleep(ACC_DELAY)

# Go immediately to set speed
def train_set_speed (speed, train=0, direction=1):
    if (direction == 1):
        motors[train].forward(speed)
        print ("Forward train "+str(train)+" speed "+str(speed))
    elif (direction == -1):
        motors[train].backward(speed)
    else:
        motors[train].stop()

def check_reed (reed, train=0):
    if (reed_switches[reed].is_pressed):
        print ("Stopping train "+str(train))
        train_slow_down (motors[train].value, train)
        return True
    else:
        return False


# Demo program - normally import this in which case this won't run
# Demo uses train 0 only
def main():
    while True:
        print ("Leaving the station")
        # Accelerate up to full speed
        train_speed_up(MAX_SPEED)
        # wait until it triggers reed switch
        print ("Going to station")
        reed_switches[0].wait_for_press()
        print ("Stopping at station")
        train_slow_down(MAX_SPEED)
        sleep(STATION_DELAY)

#Run the main function when this program is run
if __name__ == "__main__":
    main()