# This Python file uses the following encoding: utf-8

import pygame
from pygame import Surface
from Cell import Cell
from Pion import Pion

class Grid:
    cell:Cell = []
    gridWidth:int = 0
    gridHeight:int = 0
    color1:int = (255, 240, 225)
    colorId1:str = "white"
    color2:int = (110, 0, 0)
    colorId2:str = "black"
    cellSize:int = 0
    x:int = 0
    y:int = 0
    def __init__(self, gridSize, screenWidth, screenHeight):
        self.initGrid(gridSize, screenWidth, screenHeight)

    def switchColors(self):
        tempColor = self.color2
        self.color2 = self.color1
        self.color1 = tempColor
        tempColorId = self.colorId2
        self.colorId2 = self.colorId1
        self.colorId1 = tempColorId

    def initGrid(self, size, screenWidth, screenHeight):
        self.setSize(size)
        cellCount = self.gridWidth * self.gridHeight
        self.cellSize = screenWidth / self.gridWidth
        for i in range(0, cellCount):
            cellIdx:int = i
            self.x = int((i % self.gridWidth) * self.cellSize)
            if i > 0 :
                if i % self.gridWidth == 0:
                    self.y += self.cellSize
                    if size % 2 == 0 :
                        self.switchColors()
            if i % 2 == 0:
                color = self.color1
                colorId = self.colorId1
                self.originalColor = self.color1
            else:
                color = self.color2
                colorId = self.colorId2
                self.originalColor = self.color2
            c:Cell = Cell(self.x, self.y, self.cellSize, color, cellIdx, colorId, screenWidth, screenHeight)
            self.cell.append(c)

    def setSize(self, size):
        self.gridWidth = size
        self.gridHeight = size

    def getWidth(self):
        return self.gridWidth

    def renderGrid(self, screen:Surface):
         for c in self.cell:
             cell:Cell = c
             cell.render(screen)

    def getLength(self):
        return self.cell.__len__()

    def Update(self, click, idx, oldIdx):
        for c in self.cell:
            cell:Cell = c
            if click:
                self.checkIfClicked(cell, idx, oldIdx)
            self.setHighLight(cell)

    def checkIfClicked(self, c, idx, oldIdx):
        if (c.getIsOccupiedBy() == "blanc" or c.getIsOccupiedBy() == "none") and c.getColorId() == 'black':
            if c.getIdx() == idx == oldIdx and c.getIsClicked() == True:
                c.setIsClicked(False)
            elif c.getIdx() == idx == oldIdx and c.getIsClicked() == False:
                c.setIsClicked(True)
            elif c.getIdx() == idx and c.getColorId() == 'black':
                c.setIsClicked(True)
            else:
                c.setIsClicked(False)

    def setHighLight(self, c):
        originalColor = self.color2
        if c.getIsClicked() == True and c.getColorId() == 'black':
            c.setColor([240,60,30])
        if c.getIsClicked() == False and c.getColorId() == 'black':
            c.setColor(originalColor)
