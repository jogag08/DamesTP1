# This Python file uses the following encoding: utf-8
import pygame

from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import QTimer

from Grid import Grid

class Game:
    grid:Grid
    def __init__(self):
        pygame.init()
        self.timer = Timer()
        self.gameInit()
        self.shouldQuit = False
        self.grid = Grid()
        pass

    def gameInit(self):
        self.size = self.width, self.height = 800, 600
        red = [255,0,0]
        screen = pygame.display.set_mode(self.size)
        screen.fill(red)
        pass

    def initGrid(self):
        pass

    def render(self):
        self.grid.drawGrid(8,8, self.width, self.height)
        pygame.display.flip() #equivalent au render present dans SDL

        #self.screen.blit(self.maxime, self.maximerect) mettre une surface sur une autre surface

    def loop(self):
        self.timer.update()
        dt = self.timer.get_deltaTime
        self.processInput()
        #Update Actors
        self.render()
        return self.shouldQuit

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.shouldQuit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print('test') #entrer ce que la touche va faire
                    pass #entrer ce que la touche va faire

class Timer:
    _clock = None
    _dt:float = 0.016

    def __init__(self):
        self._clock = pygame.time.Clock()

    def update(self):
        self._dt = self._clock.tick(60)/1000

    def get_deltaTime(self):
        return self._dt
