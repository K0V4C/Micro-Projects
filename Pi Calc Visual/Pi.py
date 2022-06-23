import random 
import pygame
import math

width = 500
heigth = width

win = pygame.display.set_mode((width,heigth))
win.fill((255,255,255))


num_of_in = 1
total = 1
running = True
while running:
    for i in range(5):
        x = random.randrange(width)
        y = random.randrange(heigth)
        p = x -250
        q = y -250
        total += 1
        if (math.sqrt(p*p+q*q)<width/2):
            pygame.draw.circle(win,(250,0,0),(x,y),1)
            num_of_in +=1
        else:
            pygame.draw.circle(win,(0,250,0),(x,y),1)

    pygame.display.update()

    pi = 4*num_of_in / total
    print(pi)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    