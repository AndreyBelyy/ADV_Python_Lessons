
import pygame
game_over = False
MAX_X = 800
MAX_Y = 600

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN) # screen resolution
pygame.display.set_caption("My First PyGame Game! :)")

myimage = pygame.image.load("/Users/aegar/Desktop/Programming/ADV_lessons/PyGame/Knights/Knight_1/walk.png").convert()
myimage = pygame.transform.scale(myimage, (600,120)) # change image resolution

x = 500
y = 100
bg_color = (0, 0, 0) # black color for background

while game_over == False:
    for event in pygame.event.get(): # read for events
        if event.type == pygame.KEYDOWN: # if button pressed
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                x -= 5
            if event.key == pygame.K_RIGHT:
                x += 5
            if event.key == pygame.K_UP:
                y -= 5
            if event.key == pygame.K_DOWN:
                y += 5

        if event.type == pygame.MOUSEBUTTONDOWN: # move with the mouse
            x, y = event.pos

    screen.fill((bg_color))          # repaint background color with black color
    screen.blit(myimage, (x, y)) # display image
    pygame.display.flip()




