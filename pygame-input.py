import pygame, time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Pygame Test')

def takepic():
    print('Taking picture...standby')
    time.sleep(1)

def timer():
    print('TIMER')
    #Code to power the timer.
    #Add 5 seconds
    #Deduct 5 seconds

def flash():
    print('FLASH AHH HAA')
    #Turn the flash on and off

while True:
    print('Waiting')
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_UP:
                print('Adding time')
                timer()
            elif event.key == pygame.K_DOWN:
                print('Deducting time')
                timer()
            elif event.key == pygame.K_LEFT:
                print('Add flash')
                flash()
            elif event.key == pygame.K_RIGHT:
                print('Rainbow Flash')
            elif event.key == pygame.K_RETURN:
                print('Takepic')
                takepic()
        time.sleep(0.1)
