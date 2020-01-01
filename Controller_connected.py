import pygame
from time import sleep

screen = pygame.display.set_mode([10,10]) #make a 10x10 window
pygame.joystick.init() #find the joysticks
joy = pygame.joystick.Joystick(0)
joy.init()

while True:
    pygame.event.get()
    rt = joy.get_axis(5)
    lt = joy.get_axis(2)
    print(rt)
    print(lt)
    sleep(0.1) #limit the frequency to 10Hz
