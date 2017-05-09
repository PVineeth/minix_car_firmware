import RPi.GPIO as GPIO
from time import sleep
import threading

GPIO.setmode(GPIO.BOARD)

# IC1 (L293D)
Input1 = 32  # Input Pin
Input2 = 36  # Input Pin
Enable1 = 38  # Enable Pin
Input3 = 24  # IN 3
Input4 = 26  # IN 4
Enable2 = 40  # EN 2

# IC2 (L293D)
Input5 = 31  # Input Pin 1
Input6 = 33  # Input Pin 2
Enable3 = 35  # Enable Pin 1
Input7 = 23  # IN 3
Input8 = 29  # IN 4
Enable4 = 37  # EN 2


class motor:
    pwm = ['']
    start = 1
    curr_speed = 70
    gear="null"
    led = 0 # Dummy Value
    forward_status = 1 # 1 = Enable

    def __init__(self, lights):
        self.led = lights
        GPIO.setup(Input1, GPIO.OUT)
        GPIO.setup(Input2, GPIO.OUT)
        GPIO.setup(Enable1, GPIO.OUT)
        GPIO.setup(Input3, GPIO.OUT)
        GPIO.setup(Input4, GPIO.OUT)
        GPIO.setup(Enable2, GPIO.OUT)
        GPIO.setup(Input5, GPIO.OUT)
        GPIO.setup(Input6, GPIO.OUT)
        GPIO.setup(Enable3, GPIO.OUT)
        GPIO.setup(Input7, GPIO.OUT)
        GPIO.setup(Input8, GPIO.OUT)
        GPIO.setup(Enable4, GPIO.OUT)
        # For Speed/Acc
        pwm1 = GPIO.PWM(Enable1, 70)
        self.pwm.append(pwm1)
        pwm2 = GPIO.PWM(Enable2, 70)
        self.pwm.append(pwm2)
        pwm3 = GPIO.PWM(Enable3, 70)
        self.pwm.append(pwm3)
        pwm4 = GPIO.PWM(Enable4, 70)
        self.pwm.append(pwm4)

    def set_lights(self, num):
        if(num == 1): # Set Backward LED's
            self.led.back_light_backward()
        elif(num == 2):
            self.led.back_light_off()
        elif(num == 3):
            self.led.left_t_light()
        elif(num == 4):
            self.led.left_t_light_off()
        elif(num == 5):
            self.led.right_t_light()
        elif(num == 6):
            self.led.right_t_light_off()
        

    def go_forward(self):
        print(self.forward_status)
        self.set_lights(2)
        self.set_lights(4)
        self.set_lights(6)
        if(self.forward_status == 1):
            if (self.start == 1):
                self.pwm[1].start(70)  # Default Speed
                self.pwm[2].start(70)  # Default Speed
                self.pwm[3].start(70)  # Default Speed
                self.pwm[4].start(70)  # Default Speed
                self.start = self.start + 1

            print("FORWARD MOTION")
            self.gear = "FORWARD"
            # IC1
            GPIO.output(Input1, True)
            GPIO.output(Input2, False)
            GPIO.output(Enable1, True)
            # IC2
            GPIO.output(Input5, True)
            GPIO.output(Input6, False)
            GPIO.output(Enable3, True)
            # IC1
            GPIO.output(Enable2, True)
            GPIO.output(Input3, False)
            GPIO.output(Input4, True)
            # IC2
            GPIO.output(Enable4, True)
            GPIO.output(Input7, True)
            GPIO.output(Input8, False)

    def go_backward(self):
        print("BACKWARD MOTION")
        self.gear = "BACKWARD"
        # IC1
        GPIO.output(Input1, False)
        GPIO.output(Input2, True)
        GPIO.output(Enable1, True)
        # IC2
        GPIO.output(Input5, False)
        GPIO.output(Input6, True)
        GPIO.output(Enable3, True)
        # IC1
        GPIO.output(Enable2, True)
        GPIO.output(Input3, True)
        GPIO.output(Input4, False)
        # IC2
        GPIO.output(Enable4, True)
        GPIO.output(Input7, False)
        GPIO.output(Input8, True)
        self.set_lights(1)
        self.set_lights(4)
        self.set_lights(6)
    
    def go_left(self):
        print("Going Left")
        if(self.gear == "FORWARD"):
            self.go_forward()
        elif(self.gear == "BACKWARD"):
            self.go_backward()
        GPIO.output(Enable2, False)
        GPIO.output(Enable4, False)
        GPIO.output(Input3, False)
        GPIO.output(Input4, False)
        GPIO.output(Input5, False)
        GPIO.output(Input6, False)
        self.set_lights(3)
        self.set_lights(2)
        self.set_lights(6)

    def go_right(self):
        print("Going Right")
        if(self.gear == "FORWARD"):
            self.go_forward()
        elif(self.gear == "BACKWARD"):
            self.go_backward()
        GPIO.output(Enable1, False)
        GPIO.output(Enable3, False)
        GPIO.output(Input1, False)
        GPIO.output(Input2, False)
        GPIO.output(Input7, False)
        GPIO.output(Input8, False)
        self.set_lights(5)
        self.set_lights(2)
        self.set_lights(4)

    def apply_brakes(self):
        print("Applying breaks")
        self.curr_speed = int(float(self.curr_speed)) - 1
        if(self.curr_speed > 0):
            self.set_speed(self.curr_speed)
        if(self.curr_speed == 0):
            self.pwm[1].stop()
            self.pwm[2].stop()
            self.pwm[3].stop()
            self.pwm[4].stop()
       # light.back_light_on()
        # self.pwm.stop()

    def stop(self):
        print("Stopping")
        self.forward_status = 0 # 0 = Disable
        GPIO.output(Enable1, False)
        GPIO.output(Enable3, False)
        GPIO.output(Input1, False)
        GPIO.output(Input2, False)
        GPIO.output(Input7, False)
        GPIO.output(Input8, False)
        GPIO.output(Enable2, False)
        GPIO.output(Enable4, False)
        GPIO.output(Input3, False)
        GPIO.output(Input4, False)
        GPIO.output(Input5, False)
        GPIO.output(Input6, False)

    def set_speed(self, speed):
        self.curr_speed = speed
        self.pwm[1].ChangeDutyCycle(float(speed))
        self.pwm[2].ChangeDutyCycle(float(speed))
        self.pwm[3].ChangeDutyCycle(float(speed))
        self.pwm[4].ChangeDutyCycle(float(speed))
        return 0  # Return Anything to exit thread

    def set_forward_status(self):
        self.forward_status = 1
        
