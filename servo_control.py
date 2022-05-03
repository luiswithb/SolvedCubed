import time
import keyboard
from board import SCL, SDA
import busio

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

pca = PCA9685(i2c)

pca.frequency = 50

servo0 = servo.ContinuousServo(pca.channels[0])
servo1 = servo.ContinuousServo(pca.channels[1])
servo2 = servo.ContinuousServo(pca.channels[2])
servo3 = servo.ContinuousServo(pca.channels[3])
servo4 = servo.ContinuousServo(pca.channels[4])
servo5 = servo.ContinuousServo(pca.channels[5])

tCW = -1
def cw(n):
    servo0.throttle = tCW
    time.sleep(n)
    pca.channels[0].duty_cycle = 0

def cw1(n):
    servo1.throttle = tCW
    time.sleep(n)
    pca.channels[1].duty_cycle = 0

def cw2(n):
    servo2.throttle = tCW
    time.sleep(n)
    pca.channels[2].duty_cycle = 0
    
def cw3(n):
    servo3.throttle = tCW
    time.sleep(n)
    pca.channels[3].duty_cycle = 0

def cw4(n):
    servo4.throttle = tCW
    time.sleep(n)
    pca.channels[4].duty_cycle = 0

def cw5(n):
    servo5.throttle = tCW
    time.sleep(n)
    pca.channels[5].duty_cycle = 0

tCCW = 1
def ccw(n):
    servo0.throttle = tCCW
    time.sleep(n)
    pca.channels[0].duty_cycle = 0

def ccw1(n):
    servo1.throttle = tCCW
    time.sleep(n)
    pca.channels[1].duty_cycle = 0

def ccw2(n):
    servo2.throttle = tCCW
    time.sleep(n)
    pca.channels[2].duty_cycle = 0
    
def ccw3(n):
    servo3.throttle = tCCW
    time.sleep(n)
    pca.channels[3].duty_cycle = 0

def ccw4(n):
    servo4.throttle = tCCW
    time.sleep(n)
    pca.channels[4].duty_cycle = 0

def ccw5(n):
    servo5.throttle = tCCW
    time.sleep(n)
    pca.channels[5].duty_cycle = 0

def solveArray(arr):
    for i in arr:
        if i == 'D':
            ccw(0.17)
        if i == 'Di':
            cw(0.155)
            
        if i == 'L':
            ccw1(0.17)
        if i == 'Li':
            cw1(0.16)
            
        if i == 'B':
            ccw2(0.19)
        if i == 'Bi':
            cw2(0.18)
            
        if i == 'R':
            ccw3(0.1925)
        if i == 'Ri':
            cw3(0.195)
            
        if i == 'F':
            ccw4(0.2)
        if i == 'Fi':
            cw4(0.2)
            
        if i == 'U':
            ccw5(0.1525)
        if i == 'Ui':
            cw5(0.155)
            
        while not keyboard.is_pressed(' '):
            time.sleep(0.1 )
                
scramble = ['F','L','B','B','R','R','U','Bi','Ui','B','B','Ri','Bi','Ui','L','L','F','F','U','B','B','Di','F','F','L','L','U']
scramble2 = scramble[::-1]

solveArray(scramble)
    
def solveMain():
    t = 0.08
    while True:
        # servo 0
        if keyboard.is_pressed('d'):
            ccw(0)
            time.sleep(t)
        if keyboard.is_pressed('c'):
            cw(0)
            time.sleep(t)
            
        # servo 1
        if keyboard.is_pressed('l'):
            ccw1(0)
            time.sleep(t)
        if keyboard.is_pressed('.'):
            cw1(0)
            time.sleep(t)
            
        # servo 2
        if keyboard.is_pressed('b'):
            ccw2(0)
            time.sleep(t)
        if keyboard.is_pressed(' '):
            cw2(0)
            time.sleep(t)
            
        # servo 3
        if keyboard.is_pressed('4'):
            ccw3(0)
            time.sleep(t)
        if keyboard.is_pressed('r'):
            cw3(0)
            time.sleep(t)
            
        # servo 4
        if keyboard.is_pressed('f'):
            ccw4(0)
            time.sleep(t)
        if keyboard.is_pressed('v'):
            cw4(0)
            time.sleep(t)
            
        # servo 5
        if keyboard.is_pressed('u'):
            ccw5(0)
            time.sleep(t)
        if keyboard.is_pressed('j'):
            cw5(0)
            time.sleep(t)
            
        else:
            pca.channels[0].duty_cycle = 0
            pca.channels[1].duty_cycle = 0
            pca.channels[2].duty_cycle = 0
            pca.channels[3].duty_cycle = 0
            pca.channels[4].duty_cycle = 0
            pca.channels[5].duty_cycle = 0

pca.channels[0].duty_cycle = 0
pca.channels[1].duty_cycle = 0
pca.channels[2].duty_cycle = 0
pca.channels[3].duty_cycle = 0
pca.channels[4].duty_cycle = 0
pca.channels[5].duty_cycle = 0
pca.deinit()

'''
    # servo 1
    if keyboard.is_pressed('w'):
        ccw1()
        time.sleep(t)
    # servo 2
    if keyboard.is_pressed('e'):
        cw2()
        time.sleep(t)
    # servo 3
    if keyboard.is_pressed('r'):
        cw3()
        time.sleep(t)
    # servo 4
    if keyboard.is_pressed('t'):
        cw4()
        time.sleep(t)
    # servo 5
    if keyboard.is_pressed('y'):
        cw5()
        time.sleep(t)
    
    # servo 0
    if keyboard.is_pressed('a'):
        ccw()
        time.sleep(t)
    # servo 1
    if keyboard.is_pressed('s'):
        cw1()
        time.sleep(t)
    # servo 2
    if keyboard.is_pressed('d'):
        ccw2()
        time.sleep(t)
    # servo 3
    if keyboard.is_pressed('f'):
        ccw3()
        time.sleep(t)
    # servo 4
    if keyboard.is_pressed('g'):
        ccw4()
        time.sleep(t)
    # servo 5
    if keyboard.is_pressed('h'):
        ccw5()
        time.sleep(t) 
'''