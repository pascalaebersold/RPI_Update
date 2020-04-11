from time import sleep
import serial
import time
import RPi.GPIO as GPIO
import math

id = 3
a = 1

# sets the 74ls24 to send mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

# define the serial port (UART)
port = serial.Serial("/dev/ttyAMA0", baudrate=1000000, timeout=0.00005)

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
read_UART()
