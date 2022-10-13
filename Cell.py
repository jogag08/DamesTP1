# This Python file uses the following encoding: utf-8
import pygame
from pygame import Surface

class Cell:
    x:int
    y:int
    size:int
    color:int = []
    id:int
    screenW:int
    screenH:int
    colorId:str
    isClicked:bool
    def __init__(self, x, y, size, color, id, colorId, screenW, screenH):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.id = id
        self.colorId = colorId
        self.screenW = screenW
        self.screenH = screenH
        self.isClicked = False

    def render(self, screen:Surface):
        cellRect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(screen, self.color, cellRect)

    def getColorId(self):
        return self.colorId

    def getId(self):
        return self.id

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getSize(self):
        return self.size

    def getColor(self):
        return self.color

    def setColor(self, newColor:int = []):
        self.color = newColor

    def isClicked(self):
        return self.isClicked

