from tkinter import *
import tkinter.font as font
import os

root = Tk()

# define font
FontHEL20B = font.Font(family='Helvetica', size=20, weight='bold')
FontHEL50B = font.Font(family='Helvetica', size=30, weight='bold')

# toggle fullscreen
w, h = root.winfo_screenwidth(), root.winfo_screenheight()

# use the next line if you also want to get rid of the titlebar
root.overrideredirect(1)
#root.geometry("%dx%d+0+0" % (w, h))
root.geometry("480x320")

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

# Button to close the window
exitbutton = Button(text = "exit", command = close_window)
# define font for Button
exitbutton['font'] = FontHEL20B
# define place on window
exitbutton.place(x=210, y=260)


# Button to go to the left window
controllerbutton = Button(text = "Controller", command = left_window, bd=1, width = 20)
# define font for Button
controllerbutton['font'] = FontHEL50B
# define place on window
controllerbutton.place(x=0, y=80)


# Button to go to the right window
play_programm = Button(text = "Play Programm", command = right_window, bd=1, width = 20)
# define font for Button
play_programm['font'] = FontHEL50B
# define place on window
play_programm.place(x=0, y=160)

# Button to go to the right window
edit_programm = Button(text = "Edit Programm", command = right_window, bd=1, width = 20)
# define font for Button
edit_programm['font'] = FontHEL50B
# define place on window
edit_programm.place(x=0, y=240)

# Button to close the window
updatebutton = Button(text = "UPDATE", command = update_program, bd=1, width = 20)
# define font for Button
updatebutton['font'] = FontHEL50B
# define place on window
updatebutton.place(x=0, y=0)


# mainloop for tkinter
root.mainloop()
