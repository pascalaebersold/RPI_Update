import pygame
from time import sleep
import time
import serial
import RPi.GPIO as GPIO
import math
from subprocess import Popen, PIPE
from os import remove
import os

id = 1
a = 1
ar = 1
e = 0
f = 0
e1 = 0
f1 = 0
e2 = 0
f2 = 0
e3 = 0
f3 = 0
e4 = 0
f4 = 0
e5 = 0
f5 = 4
arrs=()
arrt=()
arra=()
crc2=0

# sets the 74ls24 to send mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

# define the serial port (UART)
port = serial.Serial("/dev/ttyAMA0", baudrate=1000000, timeout=0.000005)

#pygame init
pygame.init()
screen = pygame.display.set_mode((1, 1))
done = False
clock = pygame.time.Clock()
pygame.joystick.init()

def send_UART ():

    GPIO.output(17, GPIO.HIGH)
    time.sleep(0.0001)
    port.write(arrs)
    time.sleep(0.00001)
    port.write(arrt)
    time.sleep(0.00001)
    port.write(arra)
    time.sleep(0.00001)
    GPIO.output(17, GPIO.LOW)

def read_UART ():
    crc11= 255 - (id + 4 + 2 + 36 + 2)
    if crc11 < 0:
        crc12 = crc11+256
    else:
        crc12 = crc11

    arrgetp=(255, 255, id, 4, 2, 36, 2, crc12)
    global ar
    global e
    global f
    while ar==1:
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.0001)
        port.write(arrgetp)
        time.sleep(0.0001)
        port.write(arrgetp)
        time.sleep(0.0001)
        GPIO.output(17, GPIO.LOW)
        data = port.readline()
        if id == 1 and len(data) == 2 and list(data)[0] < 17:
            e = list(data)[0]
            f = list(data)[1]
            ar= 0
        if len(data) == 8 and list(data)[0]==255:
            print(list(data))
            correct = 255-list(data)[2]-list(data)[3]-list(data)[4]-list(data)[5]-list(data)[6]
            if correct < 0:
                correct = correct +256
            if correct == list(data)[-1] and list(data)[2]==id:
                f = list(data)[6]
                e = list(data)[7]
                e = 247 - e
                if e < 1:
                    if f == 0:
                        e = 255 + e
                    if f == 1:
                        e == 254 + e
                    if f == 2:
                        e = 253 + 2
                    if f == 3:
                        e = 252 + e
                ar=0
    ar=1

#array speed sets the speed for the next action
arrs = (255, 255, 4, 5, 3, 32, 61, 0, 150)
#array torque sets the torque for the next action
arrt = (255, 255, 4, 5, 3, 34, 255, 3, 207)
#array angle sets the angle/position
arra = (255, 255, 4, 5, 3, 30, 130, 1, 82)
send_UART()
time.sleep(1.1)
send_UART()
time.sleep(1.1)
#array speed sets the speed for the next action
arrs = (255, 255, 3, 5, 3, 32, 32, 0, 180)
#array torque sets the torque for the next action
arrt = (255, 255, 3, 5, 3, 34, 255, 3, 208)
#array angle sets the angle/position
arra = (255, 255, 3, 5, 3, 30, 42, 3, 169)
send_UART()
time.sleep(1.1)
send_UART()
time.sleep(1.1)
#array speed sets the speed for the next action
arrs = (255, 255, 2, 5, 3, 32, 113, 0, 100)
#array torque sets the torque for the next action
arrt = (255, 255, 2, 5, 3, 34, 255, 3, 209)
#array angle sets the angle/position
arra = (255, 255, 2, 5, 3, 30, 160, 2, 53)
send_UART()
time.sleep(1.1)
send_UART()
time.sleep(1.1)
#array speed sets the speed for the next action
arrs = (255, 255, 1, 5, 3, 32, 2, 0, 212)
#array torque sets the torque for the next action
arrt = (255, 255, 1, 5, 3, 34, 59, 1, 152)
#array angle sets the angle/position
arra = (255, 255, 1, 5, 3, 30, 0, 4, 212)
send_UART()
time.sleep(1.1)
send_UART()
time.sleep(4.1)

def read_UART_2():
    global id
    while id < 5:
        if id == 1:
            e1=e
            f1=f
        if id == 2:
            e2=e
            f2=f
        if id == 3:
            e3=e
            f3=f
        if id == 4:
            e4=e
            f4=f
        if id == 5:
            e5=e
        f5=f
    id = id + 1
    read_UART()

read_UART_2()
time.sleep(5)
print ("read_OK")

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()


        axis0 = joystick.get_axis(0)
        e1 = e1 + axis0 * 10
        if e1 > 255:
            f1 = f1 + 1
            e1 = 0
        if e1 < 0 and f1 > 0:
            f1 = f1 -1
            e1 = 255
        if e1 < 0:
            e1 = 0
        if f1 > 16:
            f1 = 16
            e1 = 255
        if f1 < 0:
            f1 = 0
        e1 = round(e1)
        crc1= 255 - (1 + 5 + 3 + 30 + e1 + f1)
        if crc1 < 0:
            crc2 = crc1+256
        else:
            crc2 = crc1
        arra= (255, 255, 1, 5, 3, 30, e1, f1, crc2)

        crc3= 255 - (1 + 5 + 3 + 32 +24 + 0)
        if crc3 < 0:
            crc4 = crc3+256
        else:
            crc4 = crc3
        arrs = (255, 255, 1, 5, 3, 32, 24, 0, crc4)

        crc5= 255 - (1 + 5 + 3 + 34 + 255 + 3)
        if crc5 < 0:
            crc6 = crc5+256
        else:
            crc6 = crc5
        arrt = (255, 255, 1, 5, 3, 34, 255, 3, crc6)
        send_UART()


        axis1 = joystick.get_axis(1)
        e2 = e2 + axis1
        if e2 > 255:
            f2 = f2+1
            e2 = 0
        if e2 < 0 and f2 > 0:
            f2 = f2-1
            e2=255
        if e2 < 0:
            e2 = 0
        if f2 > 3:
            f2 = 3
            e2 = 255
        if f2 < 0:
            f2 = 0
        e2 = round(e2)


        crc1= 255 - (2 + 5 + 3 + 30 + e2 + f2)
        if crc1 < 0:
            crc2 = crc1+256
        else:
            crc2 = crc1
        arra= (255, 255, 2, 5, 3, 30, e2, f2, crc2)

        crc3= 255 - (2 + 5 + 3 + 32 +24 + 0)
        if crc3 < 0:
            crc4 = crc3+256
        else:
            crc4 = crc3
        arrs = (255, 255, 2, 5, 3, 32, 24, 0, crc4)

        crc5= 255 - (2 + 5 + 3 + 34 + 255 + 3)
        if crc5 < 0:
            crc6 = crc5+256
        else:
            crc6 = crc5
        arrt = (255, 255, 2, 5, 3, 34, 255, 3, crc6)
        send_UART()

        axis3 = joystick.get_axis(3)
        e3 = e3 + axis3
        if e3 > 255:
            f3 = f3+1
            e3 = 0
        if e3 < 0 and f3 > 0:
            f3 = f3-1
            e3=255
        if e3 < 0:
            e3 = 0
        if f3 > 3:
            f3 = 3
            e3 = 255
        if f3 < 0:
            f3 = 0
        e3 = round(e3)


        crc1= 255 - (3 + 5 + 3 + 30 + e3 + f3)
        if crc1 < 0:
            crc2 = crc1+256
        else:
            crc2 = crc1
        arra= (255, 255, 3, 5, 3, 30, e3, f3, crc2)

        crc3= 255 - (3 + 5 + 3 + 32 +35 + 0)
        if crc3 < 0:
            crc4 = crc3+256
        else:
            crc4 = crc3
        arrs = (255, 255, 3, 5, 3, 32, 35, 0, crc4)

        crc5= 255 - (3 + 5 + 3 + 34 + 255 + 3)
        if crc5 < 0:
            crc6 = crc5+256
        else:
            crc6 = crc5
        arrt = (255, 255, 3, 5, 3, 34, 255, 3, crc6)
        send_UART()

        axis4 = joystick.get_axis(4)
        e4 = e4 + axis4
        if e4 > 255:
            f4 = f4+1
            e4 = 0
        if e4 < 0 and f4 > 0:
            f4 = f4-1
            e4=255
        if e4 < 0:
            e4 = 0
        if f4 > 3:
            f4 = 3
            e4 = 255
        if f4 < 0:
            f4 = 0
        e4 = round(e4)


        crc1= 255 - (4 + 5 + 3 + 30 + e4 + f4)
        if crc1 < 0:
            crc2 = crc1+256
        else:
            crc2 = crc1
        arra= (255, 255, 4, 5, 3, 30, e4, f4, crc2)

        crc3= 255 - (2 + 5 + 3 + 32 +24 + 0)
        if crc3 < 0:
            crc4 = crc3+256
        else:
            crc4 = crc3
        arrs = (255, 255, 4, 5, 3, 32, 24, 0, crc4)

        crc5= 255 - (4 + 5 + 3 + 34 + 255 + 3)
        if crc5 < 0:
            crc6 = crc5+256
        else:
            crc6 = crc5
        arrt = (255, 255, 4, 5, 3, 34, 255, 3, crc6)
        send_UART()

        if event.type == pygame.JOYBUTTONDOWN:

            print(event.button)

            if event.button == 0:
                os.system("python3 /home/pi/Program/STEP1.py")

            if event.button == 1:
                os.system("python3 /home/pi/Program/STEP2.py")

            if event.button == 2:
                os.system("python3 /home/pi/Program/STEP3.py")

            if event.button == 3:
                os.system("python3 /home/pi/Program/STEP4.py")

            while event.button == 5:
                e5 = e5 - 100
                if e5 > 255:
                    f5 = f5+1
                    e4 = 0
                if e5 < 0 and f5 > 0:
                    f5 = f5-1
                    e5=255
                if e5 < 0:
                    e5 = 0
                if f5 > 3:
                    f5 = 3
                    e5 = 255
                if f5 < 0:
                    f5 = 0
                e5 = round(e5)


                crc1= 255 - (5 + 5 + 3 + 30 + e5 + f5)
                if crc1 < 0:
                    crc2 = crc1+256
                else:
                    crc2 = crc1
                arra= (255, 255, 5, 5, 3, 30, e5, f5, crc2)

                crc3= 255 - (5 + 5 + 3 + 32 +24 + 0)
                if crc3 < 0:
                    crc4 = crc3+256
                else:
                    crc4 = crc3
                arrs = (255, 255, 5, 5, 3, 32, 24, 0, crc4)

                crc5= 255 - (5 + 5 + 3 + 34 + 255 + 3)
                if crc5 < 0:
                    crc6 = crc5+256
                else:
                    crc6 = crc5
                arrt = (255, 255, 5, 5, 3, 34, 255, 3, crc6)
                send_UART()

            while event.button == 4:
                e5 = e5 + 100
                if e5 > 255:
                    f5 = f5+1
                    e4 = 0
                if e5 < 0 and f5 > 0:
                    f5 = f5-1
                    e5=255
                if e5 < 0:
                    e5 = 0
                if f5 > 3:
                    f5 = 3
                    e5 = 255
                if f5 < 0:
                    f5 = 0
                e5 = round(e5)


                crc1= 255 - (5 + 5 + 3 + 30 + e5 + f5)
                if crc1 < 0:
                    crc2 = crc1+256
                else:
                    crc2 = crc1
                arra= (255, 255, 5, 5, 3, 30, e5, f5, crc2)

                crc3= 255 - (5 + 5 + 3 + 32 +24 + 0)
                if crc3 < 0:
                    crc4 = crc3+256
                else:
                    crc4 = crc3
                arrs = (255, 255, 5, 5, 3, 32, 24, 0, crc4)

                crc5= 255 - (5 + 5 + 3 + 34 + 255 + 3)
                if crc5 < 0:
                    crc6 = crc5+256
                else:
                    crc6 = crc5
                arrt = (255, 255, 5, 5, 3, 34, 255, 3, crc6)
                send_UART()


            if event.button == 9:
                done = True

            if event.button == 10:
                #array speed sets the speed for the next action
                arrs = (255, 255, 4, 5, 3, 32, 61, 0, 150)
                #array torque sets the torque for the next action
                arrt = (255, 255, 4, 5, 3, 34, 255, 3, 207)
                #array angle sets the angle/position
                arra = (255, 255, 4, 5, 3, 30, 130, 1, 82)
                send_UART()
                time.sleep(1.1)
                send_UART()
                time.sleep(1.1)
                #array speed sets the speed for the next action
                arrs = (255, 255, 3, 5, 3, 32, 32, 0, 180)
                #array torque sets the torque for the next action
                arrt = (255, 255, 3, 5, 3, 34, 255, 3, 208)
                #array angle sets the angle/position
                arra = (255, 255, 3, 5, 3, 30, 42, 3, 169)
                send_UART()
                time.sleep(1.1)
                send_UART()
                time.sleep(1.1)
                #array speed sets the speed for the next action
                arrs = (255, 255, 2, 5, 3, 32, 113, 0, 100)
                #array torque sets the torque for the next action
                arrt = (255, 255, 2, 5, 3, 34, 255, 3, 209)
                #array angle sets the angle/position
                arra = (255, 255, 2, 5, 3, 30, 160, 2, 53)
                send_UART()
                time.sleep(1.1)
                send_UART()
                time.sleep(1.1)
                #array speed sets the speed for the next action
                arrs = (255, 255, 1, 5, 3, 32, 2, 0, 212)
                #array torque sets the torque for the next action
                arrt = (255, 255, 1, 5, 3, 34, 59, 1, 152)
                #array angle sets the angle/position
                arra = (255, 255, 1, 5, 3, 30, 0, 4, 212)
                send_UART()
                time.sleep(1.1)
                send_UART()
                time.sleep(4.1)
                id = 0
                read_UART_2()

    clock.tick(50)

pygame.quit()
