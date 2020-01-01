import pygame
from time import sleep
import serial
import time
import RPi.GPIO as GPIO
import math

# define the serial port (UART)
port = serial.Serial("/dev/ttyAMA0", baudrate=1000000, timeout=3.0)

#make a 10x10 window
screen = pygame.display.set_mode([10,10])
#find the joysticks
pygame.joystick.init()
joy = pygame.joystick.Joystick(0)
joy.init()

def send_UART ():
    GPIO.output(17, GPIO.HIGH)
    port.write(arrt)
    time.sleep(0.1)
    port.write(arrs)
    time.sleep(0.1)
    port.write(arra)
    time.sleep(1)
    GPIO.output(17, GPIO.LOW)

while C > 0:
    pygame.event.get()
    rt = joy.get_axis(5)
    lt = joy.get_axis(2)
    X = joy.get_button(1)
    C = joy.get_button(2)
    PS4 = joy.get_button(12)

    if PS4 > 0:
        arra = (255, 255, 5, 5, 3, 30, 0, 0, 212)
        arrs = (255, 255, 5, 5, 3, 32, 15, 0, 195)
        arrt = (255, 255, 5, 5, 3, 34, 119, 1, 88)
        send_UART()

    sleep(0.1) #limit the frequency to 10Hz
