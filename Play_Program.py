from time import sleep
import serial
import time
import RPi.GPIO as GPIO
import math

# sets the 74ls24 to send mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

# define the serial port (UART)
port = serial.Serial("/dev/ttyAMA0", baudrate=1000000, timeout=0.00005)

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

#STEP 1 ID 1
arra = (255 ,255 ,1 ,5 ,3 ,30 ,0 ,0 ,216)
arrs = (255 ,255 ,1 ,5 ,3 ,32 ,24 ,0 ,190)
arrt = (255 ,255 ,1 ,5 ,3 ,34 ,255 ,3 ,210)
send_UART()
#STEP 1 ID 2
arra=(0, 0, 0, 0, 0, 0, 0, 0)
arrs=(0, 0, 0, 0, 0, 0, 0, 0)
arrt=(0, 0, 0, 0, 0, 0, 0, 0)
send_UART()
#STEP 1 ID 3
arra=(0, 0, 0, 0, 0, 0, 0, 0)
arrs=(0, 0, 0, 0, 0, 0, 0, 0)
arrt=(0, 0, 0, 0, 0, 0, 0, 0)
send_UART()
#STEP 1 ID 4
arra=(0, 0, 0, 0, 0, 0, 0, 0)
arrs=(0, 0, 0, 0, 0, 0, 0, 0)
arrt=(0, 0, 0, 0, 0, 0, 0, 0)
send_UART()
#STEP 1 ID 5
arra=(0, 0, 0, 0, 0, 0, 0, 0)
arrs=(0, 0, 0, 0, 0, 0, 0, 0)
arrt=(0, 0, 0, 0, 0, 0, 0, 0)
send_UART()

time.sleep(5)

#STEP 2 ID 1
arra=(0, 0, 0, 0, 0, 0, 0, 0)
arrs=(0, 0, 0, 0, 0, 0, 0, 0)
arrt=(0, 0, 0, 0, 0, 0, 0, 0)
send_UART()
#STEP 2 ID 2
arra=(0, 0, 0, 0, 0, 0, 0, 0)
arrs=(0, 0, 0, 0, 0, 0, 0, 0)
arrt=(0, 0, 0, 0, 0, 0, 0, 0)
send_UART()
#STEP 2 ID 3
arra=(0, 0, 0, 0, 0, 0, 0, 0)
arrs=(0, 0, 0, 0, 0, 0, 0, 0)
arrt=(0, 0, 0, 0, 0, 0, 0, 0)
send_UART()
#STEP 2 ID 4
arra=(0, 0, 0, 0, 0, 0, 0, 0)
arrs=(0, 0, 0, 0, 0, 0, 0, 0)
arrt=(0, 0, 0, 0, 0, 0, 0, 0)
send_UART()
#STEP 2 ID 5
arra=(0, 0, 0, 0, 0, 0, 0, 0)
arrs=(0, 0, 0, 0, 0, 0, 0, 0)
arrt=(0, 0, 0, 0, 0, 0, 0, 0)
send_UART()
