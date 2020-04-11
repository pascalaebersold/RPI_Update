import pygame
from time import sleep
import serial
import time
import RPi.GPIO as GPIO
import math
from subprocess import Popen, PIPE

a = 1
x = 0
y = 2
b = 0
v = 0
C = 0
e = 0
f = 0
d = 0
id = 5
arrs=()
arrt=()
arra=()
crc2=0
arrcw=()
arrccw=()
arrgetp=(255, 255, 1, 4, 2, 36, 2, 210)

def send_UART ():

    GPIO.output(17, GPIO.HIGH)
    time.sleep(0.0001)
    port.write(arrs)
    time.sleep(0.00001)
    port.write(arrt)
    time.sleep(0.00001)
    port.write(arra)
    time.sleep(0.00001)
    port.write(arrcw)
    time.sleep(0.00001)
    port.write(arrccw)
    time.sleep(0.00001)
    GPIO.output(17, GPIO.LOW)

def read_UART ():
    crc11= 255 - (id + 4 + 2 + 30 + 2)
    if crc11 < 0:
        crc12 = crc11+256
    else:
        crc12 = crc11
                
    arrgetp=(255, 255, id, 4, 2, 30, 2, crc12)
    global a
    global v
    global y
    while a==1:
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.0001)
        port.write(arrgetp)
        time.sleep(0.0001)
        GPIO.output(17, GPIO.LOW)
        data = port.readline()
        if len(data) == 8 and list(data)[0]==255:
            print(list(data))
            correct = 255-list(data)[2]-list(data)[3]-list(data)[4]-list(data)[5]-list(data)[6]
            if correct < 0:
                correct = correct +256
            if correct == list(data)[-1] and list(data)[2]==id:
                y = list(data)[6]
                v = list(data)[7]
                print(id,v,y)
                a=0
    a=1
    print("Read out ok")
    
# sets the 74ls24 to send mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

# define the serial port (UART)
port = serial.Serial("/dev/ttyAMA0", baudrate=1000000, timeout=0.00005)

pygame.init()
screen = pygame.display.set_mode((1, 1))
done = False
clock = pygame.time.Clock()
pygame.joystick.init()

#Read value of id 1
read_UART()
GPIO.output(17, GPIO.HIGH)
time.sleep(0.0001)
port.write(arrgetp)
time.sleep(0.0001)
GPIO.output(17, GPIO.LOW)
data = port.readline()
if len(data) ==5 and list(data)[1]== 0:
        e = list(data)[2]
        f = list(data)[3]
print(e,f)
print("init ok")


while not done:
    
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()


        axis0 = joystick.get_axis(0)
        print(axis0)


        axis1 = joystick.get_axis(1)
        e = e + axis1 * 10
        if e > 255:
            f = f + 1
            e = 0
        if e < 0 and f > 0:
            f = y -1
            e = 255
        if e < 0:
            e = 0
        if f > 16:
            f = 16
            e = 255
        if f < 0:
            f = 0
        e = round(e)
        crc1= 255 - (1 + 5 + 3 + 30 + e + f)
        if crc1 < 0:
            crc2 = crc1+256
        else:
            crc2 = crc1
        arra= (255, 255, 1, 5, 3, 30, e, f, crc2)
                
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
                
        crc7= 255 - (1 + 5 + 2 + 28 +254)
        if crc7 < 0:
            crc8 = crc7+256
        else:
            crc8 = crc7
        arrcw = (255, 255, 1, 5, 2, 28, 254, crc8)
                
        crc9= 255 - (1 + 5 + 2 + 29 + 254)
        if crc9 < 0:
            crc10 = crc9+256
        else:
            crc10 = crc9
        arrccw = (255, 255, 1, 5, 2, 29, 254, crc10)
        send_UART()


        axis3 = joystick.get_axis(3)
        print(axis3)
        

        axis4 = joystick.get_axis(4)
        x = x + axis4
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
            
                
        crc1= 255 - (id + 5 + 3 + 30 + v + y)
        if crc1 < 0:
            crc2 = crc1+256
        else:
            crc2 = crc1
        arra= (255, 255, id, 5, 3, 30, v, y, crc2)
                
        crc3= 255 - (id + 5 + 3 + 32 +24 + 0)
        if crc3 < 0:
            crc4 = crc3+256
        else:
            crc4 = crc3
        arrs = (255, 255, id, 5, 3, 32, 24, 0, crc4)
                
        crc5= 255 - (id + 5 + 3 + 34 + 255 + 3)
        if crc5 < 0:
            crc6 = crc5+256
        else:
            crc6 = crc5
        arrt = (255, 255, id, 5, 3, 34, 255, 3, crc6)
                
        crc7= 255 - (id + 5 + 2 + 28 +254)
        if crc7 < 0:
            crc8 = crc7+256
        else:
            crc8 = crc7
        arrcw = (255, 255, id, 5, 2, 28, 254, crc8)
                
        crc9= 255 - (id + 5 + 2 + 29 + 254)
        if crc9 < 0:
            crc10 = crc9+256
        else:
            crc10 = crc9
        arrccw = (255, 255, id, 5, 2, 29, 254, crc10)

        send_UART()

        if event.type == pygame.JOYBUTTONDOWN:
            
            #print(event.button)
            if event.button == 5:
                id=id+1
                if id > 5:
                    id=2
                print(id,"5")
                read_UART()
                
            if event.button == 4:
                id=id-1
                if id < 2:
                    id=5
                print(id,"4")
                read_UART()
                
            if event.button == 9:
                done=true
                
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
     
    clock.tick(40)

pygame.quit()
