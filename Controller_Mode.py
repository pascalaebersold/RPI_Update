import pygame
from time import sleep
import serial
import time
import RPi.GPIO as GPIO
import math
x = 0
y = 2
b = 0
v = 0
C = 0
arrs=()
arrt=()
arra=()
crc2=0

# sets the 74ls24 to send mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

# define the serial port (UART)
port = serial.Serial("/dev/ttyAMA0", baudrate=1000000, timeout=3.0)

#find the joysticks
screen = pygame.display.set_mode([1,1])
pygame.init
pygame.joystick.init()
joy = pygame.joystick.Joystick(0)
print("joy")
joy.init()
print("joy2")

def send_UART ():
    print("send")
    GPIO.output(17, GPIO.HIGH)
    time.sleep(0.001)
    port.write(arrs)
    print(arra)
    time.sleep(0.001)
    port.write(arrt)
    time.sleep(0.001)
    port.write(arra)
    time.sleep(0.001)
    GPIO.output(17, GPIO.LOW)

while C < 1:
    for event in pygame.event.get():
        
        if joy.get_axis(4) > 0 or joy.get_axis(4) < 0:
                b = joy.get_axis(4)
                x = x + b
                if x > 255:
                    y = y+1
                    x = 0
                if x < 0 and y > 0:
                    y = y-1
                    x=255
                if x < 0:
                    x = 0
                if y > 3:
                    y = 3
                    x = 255
                if y < 0:
                    y = 0
                v = round(x)
                print("v", v)
                crc1= 255 - (2 + 5 + 3 + 30 + v + y)
                if crc1 < 0:
                    crc2 = crc1+256
                else:
                    crc2 = crc1
                arra= (255, 255, 2, 5, 3, 30, v, y, crc2)
                arrs = (255, 255, 2, 5, 3, 32, 113, 0, 100)
                arrt = (255, 255, 2, 5, 3, 34, 255, 3, 209)
                send_UART()
            
        if event.type == pygame.JOYBUTTONDOWN:
            print(event.button)
            if event.button == 9:
                C=1
            if event.button == 10:
                #array speed sets the speed for the next action
                arrs = (255, 255, 4, 5, 3, 32, 61, 0, 150)
                #array torque sets the torque for the next action
                arrt = (255, 255, 4, 5, 3, 34, 255, 3, 207)
                #array angle sets the angle/position
                arra = (255, 255, 4, 5, 3, 30, 130, 1, 82)
                send_UART()
                #array speed sets the speed for the next action
                arrs = (255, 255, 3, 5, 3, 32, 32, 0, 180)
                #array torque sets the torque for the next action
                arrt = (255, 255, 3, 5, 3, 34, 255, 3, 208)
                #array angle sets the angle/position
                arra = (255, 255, 3, 5, 3, 30, 42, 3, 169)
                send_UART()
                #array speed sets the speed for the next action
                arrs = (255, 255, 2, 5, 3, 32, 113, 0, 100)
                #array torque sets the torque for the next action
                arrt = (255, 255, 2, 5, 3, 34, 255, 3, 209)
                #array angle sets the angle/position
                arra = (255, 255, 2, 5, 3, 30, 160, 2, 53)
                send_UART()
                #array speed sets the speed for the next action
                arrs = (255, 255, 1, 5, 3, 32, 2, 0, 212)
                #array torque sets the torque for the next action
                arrt = (255, 255, 1, 5, 3, 34, 59, 1, 152)
                #array angle sets the angle/position
                arra = (255, 255, 1, 5, 3, 30, 0, 0, 216)
                send_UART()
               
