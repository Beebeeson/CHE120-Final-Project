# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 13:34:01 2024

@author: qjf12
"""
import pygame
import sprite_anim
pygame.init()

BG=(50,50,50) 
BLACK = (0,0,0)

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("spritesheets test")

sprite_image = pygame.image.load('DinoSprites - vita.png').convert_alpha()
sprite = sprite_anim.spriteSheet(sprite_image)

#create list of frames to animate:
animation_list = []
animation_step = 8

# animation frame updates 
last_update = pygame.time.get_ticks()
animation_cooldown = 120
frame = 3

for steps in range(animation_step):
    animation_list.append(sprite.get_image(steps,24,24,3,BLACK))
    
run = True
while run:
    #fill background
    screen.fill(BG)
    
    #update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time 
        if frame >= len(animation_list):
            frame = 3
    
    #display images for test
    screen.blit(animation_list[frame],(0 ,0))
    

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    
pygame.quit()