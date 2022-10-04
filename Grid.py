# This Python file uses the following encoding: utf-8

import pygame

class Grid:
    def __init__(self):
        pass

    def drawGrid(self, width, height):
        cellSize = 40
        screenWidth = self.game.width
        screenHeight = self.game.height
        screenSize = self.width, self.height = screenWidth, screenHeight
        for i in range(0, screenWidth, cellSize):
            for j in range(0, screenHeight, cellSize):
                cell = pygame.Rect(i, j, cellSize, cellSize)
                pygame.draw.rect(screenSize, (255,255,255), cell,1)

