import RPi.GPIO as GPIO
import bluetoothdevice
import threading

import commands
import lights
#import accelerometer
import motors
import ultrasonic
import read9axis

#test = lights.light()
#test.front_lights()

#test = accelerometer.accelerometer()
#test.read_data()

#test = motors.motor()
#test.go_forward()
#test.go_backward()
#test.stop()

GPIO.setwarnings(False)

comp_obj = [''] #initialize it empty

# Create objects of all components & Add it to the comp's object list
cmd = commands.Commands()
bdevice = bluetoothdevice.device(cmd)
comp_obj.append(bdevice) # 1
light = lights.light()
motor = motors.motor(light)
comp_obj.append(motor) # 2
comp_obj.append(light) # 3
ult = ultrasonic.Ultrasonic(motor)
comp_obj.append(ult) # 4
mpu = read9axis.Mpu9250()
comp_obj.append(mpu) # 5
cmd.get_objects(comp_obj)




def bluetooth_device():
    bdevice.connect()
    bdevice.receive_data()

def ultrasonic():
    ult.controldrive()

def get_accelerometer_readings():
    mpu.crash_detect()
    
bdevicet = threading.Thread(target=bluetooth_device)
bdevicet.start()

ult_t = threading.Thread(target=ultrasonic)
ult_t.start()

mpu_t = threading.Thread(target=get_accelerometer_readings)
mpu_t.start()

ult_t.join()
bdevicet.join()
mpu_t.join()

GPIO.cleanup()
