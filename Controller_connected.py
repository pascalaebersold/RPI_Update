import pygame

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
