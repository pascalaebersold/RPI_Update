from tkinter import *
import tkinter.font as font

root = Tk()

# define font
FontHEL20B = font.Font(family='Helvetica', size=20, weight='bold')
FontHEL50B = font.Font(family='Helvetica', size=50, weight='bold')

# toggle fullscreen
w, h = root.winfo_screenwidth(), root.winfo_screenheight()

# use the next line if you also want to get rid of the titlebar
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))

# define objects on window
w = Label(root, text="It comes as standard with Python")
# define place on window
w.place(x=1500, y=2000)

# class who exits the window
def close_window ():
    root.destroy()

# class for leftbutton
def left_window ():
    root.destroy()

# class for rightbutton
def right_window ():
    root.destroy()

# class for updatebutton
def Update_program ():
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
exitbutton.place(x=700, y=930)

# Button to close the window
leftbutton = Button(text = "<", command = left_window, bd=0)
# define font for Button
leftbutton['font'] = FontHEL50B
# define place on window
leftbutton.place(x=0, y=450)

# Button to close the window
rightbutton = Button(text = ">", command = right_window, bd=0)
# define font for Button
rightbutton['font'] = FontHEL50B
# define place on window
rightbutton.place(x=1400, y=450)

# Button to close the window
rightbutton = Button(text = "UPDATE", command = update_program, bd=0)
# define font for Button
rightbutton['font'] = FontHEL50B
# define place on window
rightbutton.place(x=600, y=450)

# mainloop for tkinter
root.mainloop()
