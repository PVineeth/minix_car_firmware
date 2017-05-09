import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


class light:

    pins = [21,19,16] # 21 = Back , 19 = Left, 16 = Right

    def __init__(self):
        GPIO.setup(21, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        

    def left_t_light(self):
            GPIO.output(self.pins[1], True)
            time.sleep(0.1)
            GPIO.output(self.pins[1], False)
            time.sleep(0.5)
            return 0

    def left_t_light_off(self):
        GPIO.output(self.pins[1], False)
        return 0
    
    def right_t_light(self):
        while True:
            GPIO.output(self.pins[2], True)
            time.sleep(0.1)
            GPIO.output(self.pins[2], False)
            time.sleep(0.5)
            return 0

    def right_t_light_off(self):
        GPIO.output(self.pins[2], False)
        return 0

    def back_light_on(self):
        GPIO.output(self.pins[0], True)
        return 0

    def back_light_off(self):
        GPIO.output(self.pins[0], False)
        return 0

    def back_light_backward(self):
            GPIO.output(self.pins[0], True)
            time.sleep(0.1)
            GPIO.output(self.pins[0], False)
            time.sleep(0.5)
            return 0

    def crash_light(self):
            GPIO.output(self.pins[0], True)
            GPIO.output(self.pins[1], True)
            time.sleep(0.1)
            GPIO.output(self.pins[0], False)
            GPIO.output(self.pins[1], False)
            time.sleep(0.5)
            return 0
