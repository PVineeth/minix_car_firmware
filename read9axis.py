# coding: utf-8
## @package faboMPU9250
#  This is a library for the FaBo 9AXIS I2C Brick.
#
#  http://fabo.io/202.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import MPU9250
import time
import sys

class Mpu9250:
    
    accelo_readings = []
    mpu9250 = MPU9250.MPU9250()

    def _init_(self):
        self.get_readings()
        
        
    def get_readings(self):
        accel = self.mpu9250.readAccel()
        print (" ax = " , ( accel['x'] ))
        self.accelo_readings.insert(1,accel['x'])
        print (" ay = " , ( accel['y'] ))
        self.accelo_readings.insert(2,accel['y'])
        print (" az = " , ( accel['z'] ))
        self.accelo_readings.insert(3,accel['z'])
        time.sleep(0.5)

    def crash_detect(self):
        while True:
            old_accelo_readings = self.accelo_readings
            time.sleep(1)
            self.get_readings()
            if(old_accelo_readings[2] > 1):
                if(accelo_readings[2] < 1):
                    print("CRASH!")

#mpu = Mpu9250()
#mpu.crash_detect()
