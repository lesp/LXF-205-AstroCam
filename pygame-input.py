import pygame, time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Pygame Test')

def takepic():
    print('Taking picture...standby')
    time.sleep(1)

while True:
    print('Waiting')
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_UP:
                print('Key Pressed')
                takepic()
        time.sleep(0.1)
