# This Python file uses the following encoding: utf-8
import pygame

class Cell:
    def __init__(self, x, y, size, color, screenW, screenH):
        screenSize = pygame.display.set_mode((screenW, screenH))
        cell = pygame.Rect(x, y, size, size)
        pygame.draw.rect(screenSize, color, cell)
