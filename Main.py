from PyQt5.QtWidgets import *
import pygame
import time


pygame.init()

window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load("background.png"), [700, 500])

class Player:
    def __init__(self, x, y, texture, width, height, speed):
        self.img = pygame.img.load(texture)

while True:

    window.fill([78, 85, 134])
    window.blit(background, [0, 0])

    pygame.display.flip()

    fps.tick(60)
