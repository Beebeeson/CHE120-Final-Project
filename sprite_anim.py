# Group 42 Taixi Liu 21155457 Benson Qiu 21120579
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 15:12:58 2024

@author: qjf12
"""
import pygame
# standlone class for creating a surface with a sprite loaded.
# supports animation by inputing different frames of sprite, works with animated sprites to snatch a portion of png to display. 
#has a scaling option and can make a certain color transparent

class spriteSheet():
     def __init__(self, image):
         self.sheet = image
         
     def get_image(self, frame, width, height, scale, color):
         image = pygame.Surface((width, height)).convert_alpha()                      # draw surface to put image on
         image.blit(self.sheet, (0,0), ((frame * width),0, width,height))             # blit the image extracted from soruce sheet onto a coordinate of the screen
         image = pygame.transform.scale(image,(width*scale, height * scale))          # scale the image by a factor desired, take 4th argument as scle factor
         image.set_colorkey(color)                                                    # set the targeted color to transparent, must work with convert_alpha
         
         return image
