#!/usr/bin/env python3.4
import pygame, time
from pygame.locals import *
from picamera import PiCamera
from sense_hat import SenseHat
sense = SenseHat()
import datetime

pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Pygame Test')

def takepic(timer,toggle):
    for seconds in range(timer):
        sense.show_message(str(seconds), text_colour=[255,0,0], scroll_speed=0.05)
        time.sleep(1)
    a = str(datetime.datetime.now())
    a = a[0:19]
    flash(toggle)
    with PiCamera() as camera:
        temp = round(sense.get_temperature(),2)
        camera.resolution = (800, 600)
        camera.framerate = 24
        camera.start_preview()
        time.sleep(5)
        camera.stop_preview()
        camera.annotate_text = 'This image has a temperature of %s C' % temp
        time.sleep(0.1)
        camera.capture('/home/pi/'+(a)+'.jpg')

def flash(toggle):
    print(toggle)
    if toggle == 'on':
        sense.clear(255,255,255)
    elif toggle == 'off':
        sense.clear()
        
try:        
    timer = 0
    while True:
        #print('Waiting')
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_UP:
                    print('Adding time')
                    timer = timer + 5
                    sense.show_message(str(timer), text_colour=[255,0,0])
                elif event.key == pygame.K_DOWN:
                    print('Deducting time')
                    timer = timer - 5
                    sense.show_message(str(timer), text_colour=[255,0,0])
                elif event.key == pygame.K_LEFT:
                    print('Add flash')
                    sense.show_message('Flash ready', text_colour=[255,0,0], scroll_speed=0.05)
                    toggle = 'on'
                elif event.key == pygame.K_RIGHT:
                    flash('off')
                    toggle = 'off'
                    sense.show_message('Flash off', text_colour=[255,0,0], scroll_speed=0.05)
                elif event.key == pygame.K_RETURN:
                    print('Takepic')
                    takepic(timer,toggle)
                    flash('off')
except KeyboardInterrupt:
    pygame.display.quit()
    pygame.quit()
