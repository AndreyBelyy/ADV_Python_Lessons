"/Users/aegar/Desktop/Programming/ADV_lessons/PyGame/Snowfall"

import pygame
import random
import sys
import time

MAX_X = 1366
MAX_Y = 768
MAX_SNOW = 100
SNOW_SIZE = 64


class Snow:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 3)  # diffrent speed for falling snowflakes
        self.img_num = random.randint(1, 4)  # diffrent snowflakes
        self.image_filename = "/Users/aegar/Desktop/Programming/ADV_lessons/PyGame/Snowfall/snow" \
                              + str(self.img_num) + ".png"  # diffrent snowflakes
        self.image = pygame.image.load(self.image_filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (SNOW_SIZE, SNOW_SIZE))  # resize image

    def move_snow(self):
        self.y = self.y + self.speed
        if self.y > MAX_Y:
            self.y = (0 - SNOW_SIZE)
        i = random.randint(1, 3)
        if i == 1:  # Move snowflake right
            self.x += 1
            if self.x > MAX_X:
                self.x = (0 - SNOW_SIZE)
        elif i == 2:  # Move left
            self.x -= 1
            if self.x < (0 - SNOW_SIZE):
                self.x = MAX_SNOW

    def draw_snow(self):
        screen.blit(self.image, (self.x, self.y))

def initialize_snow(max_snow, snowfall):
    for i in range(0, max_snow):
        xx = random.randint(0, MAX_X) # adding snowflakes
        yy = random.randint(0, MAX_Y) # adding snowflakes
        snowfall.append(Snow(xx, yy))

def check_for_exit():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: # Exit if button pressed
            sys.exit()
#_______-------________

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
bg_color = (0, 0, 0)
snowfall = []

initialize_snow(MAX_SNOW, snowfall)

while True:
    screen.fill(bg_color)
    check_for_exit()
    for i in snowfall:
        i.move_snow()
        i.draw_snow()
        check_for_exit()
    time.sleep(0.0020)
    pygame.display.flip()
    check_for_exit()