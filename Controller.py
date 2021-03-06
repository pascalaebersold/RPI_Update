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


# class who exits the window
def connect_controller ():
    Popen("sudo ds4drv", shell=True)

# class who exits the window
def start ():
    Popen("python3 /home/pi/Program/Controller_Mode.py", shell=True)

# Button to close the window
connect_controller = Button(text = "Connect Controller", command = connect_controller, bd=1, width = 21)
# define font for Button
connect_controller['font'] = FontHEL50B
# define place on window
connect_controller.place(x=0, y=0)

# Button to go to the left window
start = Button(text = "Start", command = start, bd=1, width = 21)
# define font for Button
start['font'] = FontHEL50B
# define place on window
start.place(x=0, y=64)

# Button to close the window
exitbutton = Button(text = "Exit", command = close_window, width = 21)
# define font for Button
exitbutton['font'] = FontHEL50B
# define place on window
exitbutton.place(x=0, y=256)

# mainloop for tkinter
root.mainloop()
