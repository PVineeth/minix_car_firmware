import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# ULT on the left side
TRIG1 = 15
ECHO1 = 7
#ULT on the front
TRIG2 = 13
ECHO2 = 11

class Ultrasonic:

    distance_list = ['']
    motorobj = 0 #Dummy Value

    def __init__(self, motor):
        GPIO.setup(TRIG1, GPIO.OUT)
        GPIO.setup(ECHO1, GPIO.IN)
        GPIO.setup(TRIG2, GPIO.OUT)
        GPIO.setup(ECHO2, GPIO.IN)
        self.motorobj = motor

    def get_distance_1(self):
        print("Distance Measurement In Progress")
        GPIO.output(TRIG1, False)
        print("Waiting For Sensor To Settle")
        time.sleep(2)
        GPIO.output(TRIG1, True)
        time.sleep(0.00001)
        GPIO.output(TRIG1, False)
        while GPIO.input(ECHO1) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO1) == 1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance1 = pulse_duration * 17150
        distance1 = round(distance1, 2)
        print("Distance:", distance1, "cm")
        return distance1

    def get_distance_2(self):
        print("Distance Measurement In Progress: 2")
        GPIO.output(TRIG2, False)
        print("Waiting For Sensor To Settle: 2")
        time.sleep(2)
        GPIO.output(TRIG2, True)
        time.sleep(0.00001)
        GPIO.output(TRIG2, False)
        while GPIO.input(ECHO2) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO2) == 1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance2 = pulse_duration * 17150
        distance2 = round(distance2, 2)
        print("Distance:", distance2, "cm")
        return distance2

    def controldrive(self):
      while True:
        distance_2 = self.get_distance_2()
        distance_1 = self.get_distance_1()
        range1_2 = 21
        default_distance_1 = 20
        range1 = 19
        range2 = 14
        if(distance_2 > range1_2):
            print ("SAFE DISTANCE!")
            self.motorobj.set_forward_status()

       # if((distance_2)> (default_distance - 0.9) and ((distance_2)< (default_distance + 0.9))):
         #   self.distance_list.append(distance_2)

        if(distance_2 < range1):
            self.motorobj.stop()

        if(distance_1 < range2):
            self.motorobj.go_right()







#ult = ultrasonic()
#ult.get_distance_2()





















