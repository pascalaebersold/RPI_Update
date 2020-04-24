from time import sleep
import serial
import time
import RPi.GPIO as GPIO
import math
from os import remove
import os
id = 1
al = 89
sl = 90
tl = 91
a = 1
ar = 1
e = 0
f = 0

# sets the 74ls24 to send mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

# define the serial port (UART)
port = serial.Serial("/dev/ttyAMA0", baudrate=1000000, timeout=0.00005)

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
            print(list(data))
            ar= 0
        if len(data) == 8 and list(data)[0]==255:
            print(list(data))
            correct = 255-list(data)[2]-list(data)[3]-list(data)[4]-list(data)[5]-list(data)[6]
            if correct < 0:
                correct = correct +256
            if correct == list(data)[-1] and list(data)[2]==id:
                f = list(data)[6]
                e = list(data)[7]
                ar=0
    ar=1

while id < 6:
    read_UART()

    crc1= 255 - (id + 5 + 3 + 30 + e + f)
    if crc1 < 0:
        crc2 = crc1+256
    else:
        crc2 = crc1
    arra= (255, 255, id, 5, 3, 30, e, f, crc2)
                
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

    with open("/home/pi/Program/Play_Program.py") as file:
        datafile = file.readlines()
        datafile[al] = "arra = (" + ", ".join(map(str, arra)) + ")\n"
        datafile[sl] = "arrs = (" + ", ".join(map(str, arrs)) + ")\n"
        datafile[tl] = "arrt = (" + ", ".join(map(str, arrt)) + ")\n"
        newfile = open("/home/pi/Program/Play_Program_new.py", "w")
        newfile.writelines(datafile)
        newfile.close()
        remove("/home/pi/Program/Play_Program.py")
        os.rename("/home/pi/Program/Play_Program_new.py", "/home/pi/Program/Play_Program.py")
    id = id + 1
    al = al + 5
    sl = sl + 5
    tl = tl + 5

    

