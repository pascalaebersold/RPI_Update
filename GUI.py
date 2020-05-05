from tkinter import *
import tkinter.font as font
import os
from subprocess import Popen, PIPE
import serial
import RPi.GPIO as GPIO
import math
from time import sleep
import time

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

root = Tk()

# define font
FontHEL50B = font.Font(family='Helvetica', size=30, weight='bold')

# toggle fullscreen
w, h = root.winfo_screenwidth(), root.winfo_screenheight()

# use the next line if you also want to get rid of the titlebar
root.overrideredirect(1)
#root.geometry("%dx%d+0+0" % (w, h))
root.geometry("480x320")

# class for updatebutton
def update_program ():
    os.system("git clone https://github.com/pascalaebersold/RPI_Update.git /home/pi/Update")
    os.system("mv /home/pi/Program /home/pi/Programold")
    os.system("mv /home/pi/Update /home/pi/Program")
    os.system("rm -r /home/pi/Programold")
    os.system("reboot")

# class for controllebutton
def controller ():
    os.system("python3 /home/pi/Program/Controller.py")

# class for play_programmbutton
def play_programm ():
    os.system("python3 /home/pi/Program/Play_Program.py")

# class for edit_programmbutton
def edit_programm ():
    Popen("python3 /home/pi/Program/Edit_programm.py", shell=True)
    Popen("python3 /home/pi/Program/Controller_Mode.py", shell=True)

# class who exits the window
def close_window ():
    #STEP 1 ID 1
    arra = (255, 255, 1, 5, 3, 30, 0, 4, 212)
    arrs = (255, 255, 1, 5, 3, 32, 24, 0, 190)
    arrt = (255, 255, 1, 5, 3, 34, 255, 3, 210)
    send_UART()
    time.sleep(3)
    send_UART()
    time.sleep(3)
    #STEP 1 ID 2
    arra = (255, 255, 2, 5, 3, 30, 60, 3, 152)
    arrs = (255, 255, 2, 5, 3, 32, 24, 0, 189)
    arrt = (255, 255, 2, 5, 3, 34, 255, 3, 209)
    send_UART()
    time.sleep(3)
    send_UART()
    time.sleep(3)
    #STEP 1 ID 3
    arra = (255, 255, 3, 5, 3, 30, 0, 0, 212)
    arrs = (255, 255, 3, 5, 3, 32, 24, 0, 188)
    arrt = (255, 255, 3, 5, 3, 34, 255, 3, 208)
    send_UART()
    time.sleep(3)
    send_UART()
    time.sleep(3)
    #STEP 1 ID 4
    arra = (255, 255, 4, 5, 3, 30, 255, 3, 211)
    arrs = (255, 255, 4, 5, 3, 32, 24, 0, 187)
    arrt = (255, 255, 4, 5, 3, 34, 255, 3, 207)
    send_UART()
    time.sleep(3)
    send_UART()
    time.sleep(3)
    #STEP 1 ID 5
    arra = (255, 255, 5, 5, 3, 30, 0, 0, 212)
    arrs = (255, 255, 5, 5, 3, 32, 24, 0, 186)
    arrt = (255, 255, 5, 5, 3, 34, 255, 3, 206)
    send_UART()
    time.sleep(3)
    send_UART()
    time.sleep(3)
    os.system("sudo shutdown")

# Button to Update the program
updatebutton = Button(text = "Update", command = update_program, bd=1, width = 21)
# define font for Button
updatebutton['font'] = FontHEL50B
# define place on window
updatebutton.place(x=0, y=0)

# Button to go to the controller window
controllerbutton = Button(text = "Controller", command = controller, bd=1, width = 21)
# define font for Button
controllerbutton['font'] = FontHEL50B
# define place on window
controllerbutton.place(x=0, y=64)

# Button to go to the play program window
play_programm = Button(text = "Play Programm", command = play_programm, bd=1, width = 21)
# define font for Button
play_programm['font'] = FontHEL50B
# define place on window
play_programm.place(x=0, y=128)

# Button to go to the play program window
edit_programm = Button(text = "Edit Programm", command = edit_programm, bd=1, width = 21)
# define font for Button
edit_programm['font'] = FontHEL50B
# define place on window
edit_programm.place(x=0, y=192)

# Button to close the window
exitbutton = Button(text = "Exit", command = close_window, width = 21)
# define font for Button
exitbutton['font'] = FontHEL50B
# define place on window
exitbutton.place(x=0, y=256)

# mainloop for tkinter
root.mainloop()
