
import sys
import pygame
import pymunk

pygame.init()
screen = pygame.display.set_mode((600,600))

speed = 3
x = 200
y = 200


def background():
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0,0,255), (10,10,580,580))
    pygame.draw.polygon(screen, (0,255,0), [(420,20), (420,100), (70,100), (420,20)])


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    button = pygame.key.get_pressed()

    if button[pygame.K_UP]:
        y -= speed
    elif button[pygame.K_DOWN]:
        y += speed
    elif button[pygame.K_RIGHT]:
        x += speed
    elif button[pygame.K_LEFT]:
        x -= speed

    background()   
    pygame.draw.rect(screen, (255,0,0), (x,y,40,80))
    pygame.display.update()
