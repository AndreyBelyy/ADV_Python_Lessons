
import pygame

image_SIZE = 300
game_over = False
MAX_X = 1366
MAX_Y = 768

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN) # screen resolution
pygame.display.set_caption("My First PyGame Game! :)")

myimage = pygame.image.load("/Users/aegar/Desktop/Programming/ADV_lessons/PyGame/Knights/Knight_1/walk.png").convert()
myimage = pygame.transform.scale(myimage, (image_SIZE, image_SIZE)) # change image resolution

x = 500
y = 100
bg_color = (0, 0, 0) # black color for background

move_right = False
move_left = False
move_up = False
move_down = False

while game_over == False:
    for event in pygame.event.get():     # read for events
        if event.type == pygame.KEYDOWN: # if button pressed
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True

        if event.type == pygame.KEYUP:    # if button unpressed
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

    if move_left == True:
        x -= 1
        if x < 0:
             x = 0
    if move_right == True:
        x += 1
        if x > MAX_X - image_SIZE:
             x = MAX_X - image_SIZE
    if move_up == True:
        y -= 1
        if y < 0:
             y = 0
    if move_down == True:
        y += 1
        if y > MAX_Y - image_SIZE:
             y = MAX_Y - image_SIZE


    if event.type == pygame.MOUSEBUTTONDOWN: # move with the mouse
        x, y = event.pos




    screen.fill((bg_color))          # repaint background color with black color
    screen.blit(myimage, (x, y)) # display image
    pygame.display.flip()




