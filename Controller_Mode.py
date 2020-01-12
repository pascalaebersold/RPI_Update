import pygame
from time import sleep
import serial
import time
import RPi.GPIO as GPIO
import math

C = 0

# sets the 74ls24 to send mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

# define the serial port (UART)
port = serial.Serial("/dev/ttyAMA0", baudrate=1000000, timeout=3.0)

#make a 10x10 window
screen = pygame.display.set_mode([10,10])
#find the joysticks
pygame.joystick.init()
joy = pygame.joystick.Joystick(0)
joy.init()

def send_UART ():
    strs = bytearray(arrs)
    strt = bytearray(arrt)
    stre = bytearray(arre)
    stra = bytearray(arra)
    GPIO.output(17, GPIO.HIGH)
    port.write(strs)
    time.sleep(0.1)
    port.write(strt)
    time.sleep(0.1)
    port.write(stre)
    time.sleep(0.1)
    port.write(stra)
    time.sleep(0.1)
    GPIO.output(17, GPIO.LOW)

while C > 0:
    pygame.event.get()
    rt = joy.get_axis(5)
    lt = joy.get_axis(2)
    X = joy.get_button(1)
    C = joy.get_button(2)
    PS4 = joy.get_button(12)

    if PS4 > 0:
        #array speed sets the speed for the next action
        arrs = (255, 255, 4, 5, 3, 32, 8, 0, 203)
        #array torque sets the torque for the next action
        arrt = (255, 255, 4, 5, 3, 34, 255, 3, 207)
        #array enable sets the motor to listen mode so that he can execute a movment
        arre = (255, 255, 4, 2, 5, 24, 0, 220)
        #array angle sets the angle/position
        arra = (255, 255, 4, 5, 3, 30, 130, 1, 82)
        send_UART()
        #array speed sets the speed for the next action
        arrs = (255, 255, 3, 5, 3, 30, 30, 3, 181)
        #array torque sets the torque for the next action
        arrt = (255, 255, 3, 5, 3, 34, 255, 3, 208)
        #array enable sets the motor to listen mode so that he can execute a movment
        arre = (255, 255, 3, 2, 5, 24, 0, 221)
        #array angle sets the angle/position
        arra = (255, 255, 3, 5, 3, 34, 255, 3, 208)
        send_UART()
        #array speed sets the speed for the next action
        arrs = (255, 255, 2, 5, 3, 32, 8, 0, 205)
        #array torque sets the torque for the next action
        arrt = (255, 255, 2, 5, 3, 34, 255, 3, 209)
        #array enable sets the motor to listen mode so that he can execute a movment
        arre = (255, 255, 2, 2, 5, 24, 0, 222)
        #array angle sets the angle/position
        arra = (255, 255, 2, 5, 3, 30, 160, 2, 53)
        send_UART()
        #array speed sets the speed for the next action
        arrs = (255, 255, 1, 5, 3, 32, 2, 0, 212)
        #array torque sets the torque for the next action
        arrt = (255, 255, 1, 5, 3, 34, 0, 2, 210)
        #array enable sets the motor to listen mode so that he can execute a movment
        arre = (255, 255, 1, 2, 5, 24, 0, 223)
        #array angle sets the angle/position
        arra = (255, 255, 1, 5, 3, 30, 0, 0, 216)
        send_UART()

    sleep(0.1) #limit the frequency to 10Hz
