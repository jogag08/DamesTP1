# This Python file uses the following encoding: utf-8
import pygame
from pygame import Surface

class Cell:
    x:int
    y:int
    size:int
    color:int = []
    screenW:int
    screenH:int
    def __init__(self, x, y, size, color, screenW, screenH):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.screenW = screenW
        self.screenH = screenH

    def renderCell(self, screen:Surface):
        cellRect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(screen, self.color, cellRect)

