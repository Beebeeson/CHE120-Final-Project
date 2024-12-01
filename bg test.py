# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 13:25:39 2024 by Benson Qiu

reference: "Coding With Russ" on YouTube:
"PyGame Beginner Tutorial in Python - 3D Background Effect with Parallax Scrolling"

"""
import pygame
pygame.init()

clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((800,450))
pygame.display.set_caption("parallax")



#define game variables
scroll = 0.2

bg_layers = []
for i in range (1,6):
    bg_img = pygame.image.load(f'plx-{i}.png').convert_alpha()
    bg_img = pygame.transform.scale (bg_img, (384*2,216*2))
    bg_layers.append(bg_img)
bg_width = bg_layers[0].get_width()


def draw_bg():
    for x in range(50):
        speed = 0.5
        for i in bg_layers:
            screen.blit(i,((x*bg_width)-scroll*speed,0))
            speed += 0.25

# game loop
run = True

while run:
    clock.tick(FPS)
    draw_bg()
    scroll += 2.5
    
    #draw a simple ground
    pygame.draw.rect(screen,(92,64,51),(0,430,800,20))
    
# event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()