# This Python file uses the following encoding: utf-8
import pygame

from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import QTimer

from Grid import Grid

class Game:
    grid : Grid()
    def __init__(self):
        pygame.init()
        self.timer = Timer()
        self.gameInit()
        self.shouldQuit = False
        pass

    def gameInit(self):
        self.size = self.width, self.height = 800, 600
        self.black = [0,0,0]

        self.screen = pygame.display.set_mode(self.size)
        pass

    def initGrid(self):
        self.grid.drawGrid(self.width, self.height)

    def render(self):
        self.screen.fill(self.black)
        self.grid.drawGrid()
        #self.screen.blit(self.maxime, self.maximerect) mettre une surface sur une autre surface
        pygame.display.flip() #equivalent au render present dans SDL

    def loop(self):
            self.timer.update()
            dt = self.timer.get_deltaTime()

            self.processInput()
            #Update Actors
            self.render()
            return self.shouldQuit

class Timer:
    _clock = None
    _dt:float = 0.016

    def __init__(self):
        self._clock = pygame.time.Clock()

    def update(self):
        self._dt = self._clock.tick(60)/1000

    def get_deltaTime(self):
        return self._dt
