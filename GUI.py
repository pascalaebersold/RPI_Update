from tkinter import *
import tkinter.font as font
import os
import pygame

root = Tk()
pygame.init()

# define font
FontHEL20B = font.Font(family='Helvetica', size=20, weight='bold')
FontHEL50B = font.Font(family='Helvetica', size=50, weight='bold')

j = pygame.joystick.Joystick(0)
j.init()

# toggle fullscreen
w, h = root.winfo_screenwidth(), root.winfo_screenheight()

# use the next line if you also want to get rid of the titlebar
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))

#get height and width
h=root.winfo_screenheight()
h100=h/100
w=root.winfo_screenwidth()
w100=w/100

#define variable for screen rotation
left=0
right=0

# class who exits the window
def close_window ():
    root.destroy()

# class for leftbutton
def left_window ():
    if left < 3 :
        left=left+1

# class for rightbutton
def right_window ():
    if right > 1:
        right=right+1

# class for updatebutton
def update_program ():
    os.system("git clone https://github.com/pascalaebersold/RPI_Update.git /home/pi/Update")
    os.system("mv /home/pi/Program /home/pi/Programold")
    os.system("mv /home/pi/Update /home/pi/Program")
    os.system("rm -r /home/pi/Programold")
    os.system("reboot")

if j.get_button(1):
    update_program()

# Button to close the window
exitbutton = Button(text = "exit", command = close_window)
# define font for Button
exitbutton['font'] = FontHEL20B
# define place on window
exitbutton.place(x=w/2-w100*2.5, y=h-h100*5)

# Button to go to the left window
leftbutton = Button(text = "<", command = left_window, bd=0)
# define font for Button
leftbutton['font'] = FontHEL50B
# define place on window
leftbutton.place(x=0, y=h/2-h100*2)

# Button to go to the right window
rightbutton = Button(text = ">", command = right_window, bd=0)
# define font for Button
rightbutton['font'] = FontHEL50B
# define place on window
rightbutton.place(x=w-w100*6, y=h/2-h100*2)

# Button to close the window
rightbutton = Button(text = "UPDATE", command = update_program, bd=0)
# define font for Button
rightbutton['font'] = FontHEL50B
# define place on window
rightbutton.place(x=w/2-w100*30, y=h/2-h100*2)

# mainloop for tkinter
root.mainloop()
