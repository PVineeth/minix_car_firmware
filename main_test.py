import RPi.GPIO as GPIO
import bluetoothdevice
import threading

import commands
import lights
#import accelerometer
import motors
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

#comp_obj = [''] #initialize it empty

# Create objects of all components & Add it to the comp's object list
#cmd = commands.Commands()
#bdevice = bluetoothdevice.device(cmd)
#comp_obj.append(bdevice) # 1
#light = lights.light()
#light.back_light_backward()
#motor = motors.motor(light)
#comp_obj.append(motor) # 2
#comp_obj.append(light) # 3
#cmd.get_objects(comp_obj)
mpu = read9axis.Mpu9250()
mpu.get_readings()




#def bluetooth_device():
 #   bdevice.connect()
  #  bdevice.receive_data()

#bdevicet = threading.Thread(target=bluetooth_device)
#bdevicet.start()
#bdevicet.join()


GPIO.cleanup()
