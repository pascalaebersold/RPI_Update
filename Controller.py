from tkinter import *
import tkinter.font as font
import os
import pygame
import sys

a=".."

root = Tk()

os.spawnl(os.P_DETACH, "sudo ds4drv")
pygame.joystick.init() #find the joysticks
joy = pygame.joystick.Joystick(0)
joy.init()
if(joy.get_name()=='Sony Entertainment Wireless Controller'):
    a="DS4 connected"
else:
    a="Not a DS4"

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

# Button to close the window
controller_status_label = label(text = a, width = 21)
# define font for Button
controller_status_label['font'] = FontHEL50B
# define place on window
controller_status_label.place(x=0, y=194)

# Button to close the window
exitbutton = Button(text = "Exit", command = close_window, width = 21)
# define font for Button
exitbutton['font'] = FontHEL50B
# define place on window
exitbutton.place(x=0, y=256)

# mainloop for tkinter
root.mainloop()
