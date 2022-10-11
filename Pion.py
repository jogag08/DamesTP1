# This Python file uses the following encoding: utf-8

import pygame
from pygame import Surface
from Cell import Cell

class Pion(Cell):
    image:str
    type:str
    def __init__(self, x, y ,size, color, id, colorId, screenW, screenH, image:str):   #ARGUMENTS POUR CELL def __init__(self, x, y, size, color, id, colorId, screenW, screenH):
        super().__init__(x, y, size, color, id, colorId, screenW, screenH)
        self.setPionImage(image)
        self.setType()

    def setPionImage(self, path:str):
        self.image = pygame.image.load(path)

    def renderPion(self, screen:Surface, cellSize):
        resizedImage = pygame.transform.scale(self.image, (cellSize, cellSize))
        screen.blit(resizedImage, (self.x, self.y))

    def setType(self):
        self.type = "pion"

    def Update(self):
        pass

