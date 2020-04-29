from tkinter import *
import tkinter.font as font
import os
import pygame
import sys
from subprocess import Popen, PIPE

root = Tk()

# define font
FontHEL50B = font.Font(family='Helvetica', size=30, weight='bold')

# toggle fullscreen
w, h = root.winfo_screenwidth(), root.winfo_screenheight()

# use the next line if you also want to get rid of the titlebar
root.overrideredirect(1)
#root.geometry("%dx%d+0+0" % (w, h))
root.geometry("480x320")

# class who exits the window
def close_window ():
    root.destroy()
    pygame.quit()
    Popen("sudo pkill -9 -f Controller_Mode.py", shell=True)

def step1 ():
    Popen("sudo pkill -9 -f Controller_Mode.py", shell=True)
    os.system("python3 /home/pi/Program/STEP1.py")
    Popen("python3 /home/pi/Program/Controller_Mode.py", shell=True)

def step2 ():
    Popen("sudo pkill -9 -f Controller_Mode.py", shell=True)
    os.system("python3 /home/pi/Program/STEP2.py")
    Popen("python3 /home/pi/Program/Controller_Mode.py", shell=True)

def step3 ():
    Popen("sudo pkill -9 -f Controller_Mode.py", shell=True)
    os.system("python3 /home/pi/Program/STEP3.py")
    Popen("python3 /home/pi/Program/Controller_Mode.py", shell=True)

def step4 ():
    Popen("sudo pkill -9 -f Controller_Mode.py", shell=True)
    os.system("python3 /home/pi/Program/STEP4.py")
    Popen("python3 /home/pi/Program/Controller_Mode.py", shell=True)

# Button to Update the program
updatebutton = Button(text = "STEP 1", command = step1, bd=1, width = 21)
# define font for Button
updatebutton['font'] = FontHEL50B
# define place on window
updatebutton.place(x=0, y=0)

# Button to go to the controller window
controllerbutton = Button(text = "STEP 2", command = step2, bd=1, width = 21)
# define font for Button
controllerbutton['font'] = FontHEL50B
# define place on window
controllerbutton.place(x=0, y=64)

# Button to go to the play program window
play_programm = Button(text = "STEP 3", command = step3, bd=1, width = 21)
# define font for Button
play_programm['font'] = FontHEL50B
# define place on window
play_programm.place(x=0, y=128)

# Button to go to the play program window
edit_programm = Button(text = "STEP 4", command = step4, bd=1, width = 21)
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
