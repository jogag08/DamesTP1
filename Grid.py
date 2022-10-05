# This Python file uses the following encoding: utf-8

import pygame
from Cell import Cell

class Grid:
    cell:Cell = []
    def __init__(self):
        pass

    def drawGrid(self,gridWidth, gridHeight, screenWidth, screenHeight):
        color1 = (250, 230, 205)
        color2 = (115, 65, 0)
        cellSize = 50
        cellCount = gridWidth * gridHeight
        for i in range(0, cellCount):
            x = i % gridWidth * gridWidth
            y = i / gridWidth * gridHeight
            print(x)
            if i % 2 == 0:
                color = color1
            else:
                color = color2
            c:Cell = Cell(x, y, cellSize, color, screenWidth, screenHeight)
            self.cell.append(c)
