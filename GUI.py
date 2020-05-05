from tkinter import *
import tkinter.font as font
import os
from subprocess import Popen, PIPE

os.system("vncserver -randr=1920x1080")

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
    root.destroy()

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
