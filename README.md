# MiniX Car Firmware

I made the MiniX Car for my IoT project. The ultrasonic sensors (HC-SR04) fitted on to the car on the front & onto the left can measure the distance of objects in front of it and to the left of it.

The car is also fitted with four led's. One on the front left which blinks when the car is turning left and one the front right which when the car is turning right. The other two led's on the back switch on when the brake is pressed.

Accelerometer/Gyroscope/Magnetometer sensor (MPU-6050) is also fitted onto the car.

Video: https://www.youtube.com/watch?v=wNm8S-7B3EQ

# Usage

In terminal type
```
sudo python3 main.py
```

Then open the MiniX Car Control App (Requires Android 6.0 or greater) and it automatically connects to the "raspberrypi" using bluetooth.

You can control the car using the buttons in the app.
