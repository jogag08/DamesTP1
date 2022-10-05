# This Python file uses the following encoding: utf-8

import pygame
from pygame import Surface
from Cell import Cell

class Grid:
    cell:Cell = []
    def __init__(self, gridWidth, gridHeight, screenWidth, screenHeight):
        self.initGrid(gridWidth, gridHeight, screenWidth, screenHeight)

    def initGrid(self,gridWidth, gridHeight, screenWidth, screenHeight):
        color1 = (250, 230, 205)
        color2 = (115, 65, 0)
        cellSize = 125
        cellCount = gridWidth * gridHeight
        for i in range(0, cellCount):
            x:int = int((i % gridWidth) * cellSize)
            y:int = int((i / gridWidth) * cellSize)
            print(str(y))
            if i % 2 == 0 && i % 8 == 0:
                color = color1
            else:
                color = color2
            c:Cell = Cell(x, y, cellSize, color, screenWidth, screenHeight)
            self.cell.append(c)


    def renderGrid(self, screen:Surface):
         for c in self.cell:
             cell:Cell = c
             cell.renderCell(screen)


