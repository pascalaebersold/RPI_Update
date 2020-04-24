from time import sleep
import serial
import time
import RPi.GPIO as GPIO
import math

global arra
global arrs
global arrt
arra=()
arrs=()
arrt=()

# sets the 74ls24 to send mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

# define the serial port (UART)
port = serial.Serial("/dev/ttyAMA0", baudrate=1000000, timeout=0.00005)

def send_UART ():
    GPIO.output(17, GPIO.HIGH)
    time.sleep(0.001)
    port.write(arrs)
    time.sleep(0.001)
    port.write(arrt)
    time.sleep(0.001)
    port.write(arra)
    time.sleep(0.001)
    GPIO.output(17, GPIO.LOW)

#STEP 1 ID 1
arra = (255, 255, 1, 5, 3, 30, 12, 213, 247)
arrs = (255, 255, 1, 5, 3, 32, 24, 0, 190)
arrt = (255, 255, 1, 5, 3, 34, 255, 3, 210)
send_UART()
#STEP 1 ID 2
arra = (255, 255, 2, 5, 3, 30, 142, 1, 72)
arrs = (255, 255, 2, 5, 3, 32, 24, 0, 189)
arrt = (255, 255, 2, 5, 3, 34, 255, 3, 209)
send_UART()
#STEP 1 ID 3
arra = (255, 255, 3, 5, 3, 30, 44, 0, 170)
arrs = (255, 255, 3, 5, 3, 32, 24, 0, 188)
arrt = (255, 255, 3, 5, 3, 34, 255, 3, 208)
send_UART()
#STEP 1 ID 4
arra = (255, 255, 4, 5, 3, 30, 52, 2, 159)
arrs = (255, 255, 4, 5, 3, 32, 24, 0, 187)
arrt = (255, 255, 4, 5, 3, 34, 255, 3, 207)
send_UART()
#STEP 1 ID 5
arra = (255, 255, 5, 5, 3, 30, 220, 0, 248)
arrs = (255, 255, 5, 5, 3, 32, 24, 0, 186)
arrt = (255, 255, 5, 5, 3, 34, 255, 3, 206)
send_UART()

time.sleep(3)

#STEP 2 ID 1
arra = (255, 255, 1, 5, 3, 30, 0, 249, 223)
arrs = (255, 255, 1, 5, 3, 32, 24, 0, 190)
arrt = (255, 255, 1, 5, 3, 34, 255, 3, 210)
send_UART()
#STEP 2 ID 2
arra = (255, 255, 2, 5, 3, 30, 56, 1, 158)
arrs = (255, 255, 2, 5, 3, 32, 24, 0, 189)
arrt = (255, 255, 2, 5, 3, 34, 255, 3, 209)
send_UART()
#STEP 2 ID 3
arra = (255, 255, 3, 5, 3, 30, 117, 0, 97)
arrs = (255, 255, 3, 5, 3, 32, 24, 0, 188)
arrt = (255, 255, 3, 5, 3, 34, 255, 3, 208)
send_UART()
#STEP 2 ID 4
arra = (255, 255, 4, 5, 3, 30, 159, 2, 52)
arrs = (255, 255, 4, 5, 3, 32, 24, 0, 187)
arrt = (255, 255, 4, 5, 3, 34, 255, 3, 207)
send_UART()
#STEP 2 ID 5
arra = (255, 255, 5, 5, 3, 30, 245, 0, 223)
arrs = (255, 255, 5, 5, 3, 32, 24, 0, 186)
arrt = (255, 255, 5, 5, 3, 34, 255, 3, 206)
send_UART()

time.sleep(3)

#STEP 3 ID 1
arra = (255, 255, 1, 5, 3, 30, 0, 249, 223)
arrs = (255, 255, 1, 5, 3, 32, 24, 0, 190)
arrt = (255, 255, 1, 5, 3, 34, 255, 3, 210)
send_UART()
#STEP 3 ID 2
arra = (255, 255, 2, 5, 3, 30, 55, 1, 159)
arrs = (255, 255, 2, 5, 3, 32, 24, 0, 189)
arrt = (255, 255, 2, 5, 3, 34, 255, 3, 209)
send_UART()
#STEP 3 ID 3
arra = (255, 255, 3, 5, 3, 30, 116, 0, 98)
arrs = (255, 255, 3, 5, 3, 32, 24, 0, 188)
arrt = (255, 255, 3, 5, 3, 34, 255, 3, 208)
send_UART()
#STEP 3 ID 4
arra = (255, 255, 4, 5, 3, 30, 159, 2, 52)
arrs = (255, 255, 4, 5, 3, 32, 24, 0, 187)
arrt = (255, 255, 4, 5, 3, 34, 255, 3, 207)
send_UART()
#STEP 3 ID 5
arra = (255, 255, 5, 5, 3, 30, 245, 0, 223)
arrs = (255, 255, 5, 5, 3, 32, 24, 0, 186)
arrt = (255, 255, 5, 5, 3, 34, 255, 3, 206)
send_UART()

time.sleep(3)

#STEP 4 ID 1
arra = (255, 255, 1, 5, 3, 30, 0, 250, 222)
arrs = (255, 255, 1, 5, 3, 32, 24, 0, 190)
arrt = (255, 255, 1, 5, 3, 34, 255, 3, 210)
send_UART()
#STEP 4 ID 2
arra = (255, 255, 2, 5, 3, 30, 55, 1, 159)
arrs = (255, 255, 2, 5, 3, 32, 24, 0, 189)
arrt = (255, 255, 2, 5, 3, 34, 255, 3, 209)
send_UART()
#STEP 4 ID 3
arra = (255, 255, 3, 5, 3, 30, 116, 0, 98)
arrs = (255, 255, 3, 5, 3, 32, 24, 0, 188)
arrt = (255, 255, 3, 5, 3, 34, 255, 3, 208)
send_UART()
#STEP 4 ID 4
arra = (255, 255, 4, 5, 3, 30, 159, 2, 52)
arrs = (255, 255, 4, 5, 3, 32, 24, 0, 187)
arrt = (255, 255, 4, 5, 3, 34, 255, 3, 207)
send_UART()
#STEP 4 ID 5
arra = (255, 255, 5, 5, 3, 30, 245, 0, 223)
arrs = (255, 255, 5, 5, 3, 32, 24, 0, 186)
arrt = (255, 255, 5, 5, 3, 34, 255, 3, 206)
send_UART()
