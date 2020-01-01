from tkinter import *
import tkinter.font as font
import os
import pygame

root = Tk()

#initializes pygame
pygame.init()

#creats a controller object
controller = pygame.joystick.Joystick(1)

#initializes the controller
controller.init()

def scale_servo(x):

        # used to scale -1,1 to 0,180
        y = round((30-70)*x+1/1+1+70,2)

        return y

try:
    while True:
        events = pygame.event.get()
        for event in events:
            angle = scale_servo(controller.get_axis(0))
            steering.angle = angle
            print("Angle: {}".format(angle))
            if event.type == pygame.JOYBUTTONDOWN:
                if controller.get_button(0):
                    root.destroy()
                elif controller.get_button(1):
                    print("Circle Pressed")
                elif controller.get_button(2):
                    print("Triangle Pressed")
                elif controller.get_button(3):
                    print("Square Pressed")
                elif controller.get_button(4):
                    print("L1 Pressed")
                elif controller.get_button(5):
                    print("R1 Pressed")
                elif controller.get_button(6):
                    print("L2 Pressed")
                elif controller.get_button(7):
                    print("R2 Pressed")
                elif controller.get_button(8):
                    print("SHARE Pressed")
                elif controller.get_button(9):
                    print("OPTIONS Pressed")
                elif controller.get_button(10):
                    print("Power Button Pressed")
                elif controller.get_button(11):
                    print("Left Analog Pressed")
                elif controller.get_button(12):
                    print("Right Analog Pressed")

            elif event.type == pygame.JOYBUTTONUP:
                print("Button Released")

except KeyboardInterrupt:
    print("EXITING NOW")
    controller.quit()

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
exitbutton = Button(text = "Exit", command = close_window, width = 21)
# define font for Button
exitbutton['font'] = FontHEL50B
# define place on window
exitbutton.place(x=0, y=256)

# mainloop for tkinter
root.mainloop()
