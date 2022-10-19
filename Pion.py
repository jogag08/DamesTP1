# This Python file uses the following encoding: utf-8

import pygame
from pygame import Surface
from Cell import Cell

class Pion(Cell):
    __image:str
    __type:str
    __team:str
    __gridPosition:int
    __isSelected:bool
    __isAlive:bool
    def __init__(self, x, y ,size, color, idx, colorId, screenW, screenH, image, type, team, gridPosition):
        super().__init__(x, y, size, color, idx, colorId, screenW, screenH)
        self.setPionImage(image)
        self.setType(type)
        self.setTeam(team)
        self.setGridPosition(gridPosition)
        self.setIsSelected(False)
        self.setIsAlive(True)

    def setPionImage(self, path:str):
        self.image = pygame.image.load(path)

    def renderPion(self, screen:Surface, cellSize):
        resizedImage = pygame.transform.scale(self.image, (cellSize, cellSize))
        screen.blit(resizedImage, (self._x, self._y))

    def setType(self, t):
        self.__type = t

    def getType(self):
        return self.__type

    def setTeam(self, t):
        self.__team = t

    def getTeam(self):
        return self.__team

    def setIdx(self, newIdx):
        self._idx = newIdx

    def setGridPosition(self, p):
        self.__gridPosition = p

    def getGridPosition(self):
        return self.__gridPosition

    def setIsSelected(self, b):
        self.__isSelected = b

    def getIsSelected(self):
        return self.__isSelected

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def Move(self, newX, newY):
        self._x = newX
        self._y = newY

    def setIsAlive(self,b):
        self.__isAlive = b

    def getIsAlive(self):
        return self.__isAlive

