# This Python file uses the following encoding: utf-8
import pygame
from pygame import Surface

class Cell:
    _x:int
    _y:int
    _size:int
    _color:int = []
    _idx:int
    _screenW:int
    _screenH:int
    _colorId:str
    _isClicked:bool
    _isOccupiedBy:str
    __isAvailable:bool
    __dictId:int
    def __init__(self, x, y, size, color, idx, colorId, screenW, screenH):
        self._x = x
        self._y = y
        self._size = size
        self._color = color
        self._idx = idx
        self._colorId = colorId
        self._screenW = screenW
        self._screenH = screenH
        self._isClicked = False
        self._isOccupiedBy = "none"
        self.__isAvailable = False
        self.__dictId = 0

    def render(self, screen:Surface):
        cellRect = pygame.Rect(self._x, self._y, self._size, self._size)
        pygame.draw.rect(screen, self._color, cellRect)

    def getColorId(self):
        return self._colorId

    def getIdx(self):
        return self._idx

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getSize(self):
        return self._size

    def getColor(self):
        return self._color

    def setColor(self, newColor:int = []):
        self._color = newColor

    def setIsClicked(self, newBool):
        self._isClicked = newBool

    def getIsClicked(self):
        return self._isClicked

    def setIsOccupiedBy(self, team):
        self._isOccupiedBy = team

    def getIsOccupiedBy(self):
        return self._isOccupiedBy

    def setDictId(self, id):
        self.__dictId = id

    def getDictId(self):
        return self.__dictId

