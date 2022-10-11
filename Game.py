# This Python file uses the following encoding: utf-8
import pygame

from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import QTimer
from pygame import Surface

from Grid import Grid
from Pion import Pion

class Game:
    grid:Grid
    listCellsNoirs = []
    pion:Pion = []
    mousePos:int = []
    idx:int
    screen:Surface
    def __init__(self):
        pygame.init()
        self.timer = Timer()
        self.gameInit()
        self.shouldQuit = False
        self.grid = Grid(8, self.width, self.height)
        self.getCellsNoirs()
        self.initPions(12)

    def gameInit(self):
        self.size = self.width, self.height = 800, 800
        red = [255,0,0]
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill(red)
        pass

    def render(self):
        self.grid.renderGrid(self.screen)
        for i in range(self.pion.__len__()):
            self.pion[i].renderPion(self.screen, self.grid.cell[i].getSize())
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
            self.setMousePosOnClick(event)
            #self.setClickedCell()

    def getCellsNoirs(self):
        for i in range(self.grid.getLength()):
            if self.grid.cell[i].getColorId() == "black":
                cn = self.grid.cell[i]
                self.listCellsNoirs.append(cn)

    def initPions(self, nbrPionsJoueur):
        for i in range(nbrPionsJoueur): #initialisation des pions
            xNoir = self.listCellsNoirs[i].getX()
            yNoir = self.listCellsNoirs[i].getY()
            xBlanc = self.listCellsNoirs[self.listCellsNoirs.__len__()- 1 - i].getX()
            yBlanc = self.listCellsNoirs[self.listCellsNoirs.__len__()- 1 - i].getY()
            size = self.listCellsNoirs[i].getSize()
            color = (255,255,255)
            colorId = self.listCellsNoirs[i].getColorId()
            id = i
            imgNoir = "pionNoir.png"
            imgBlanc = "pionBlanc.png"
            pn:Pion = Pion(xNoir, yNoir, size, color, id, colorId, self.width, self.height, imgNoir)
            pb:Pion = Pion(xBlanc, yBlanc, size, color, id, colorId, self.width, self.height, imgBlanc)
            self.pion.append(pn)
            self.pion.append(pb)

    def setMousePosOnClick(self, ev):
        if ev.type == pygame.MOUSEBUTTONUP:
            self.mousePos = pygame.mouse.get_pos()

    def getMousePosXOnClick(self):
        return self.mousePos[0]

    def getMousePosYOnClick(self):
        return self.mousePos[1]

    def getClickedCellIdx(self):
        sizeCell = self.grid.cell[0].getSize()
        gridWidth:int = self.grid.getWidth()
        x:int = int(self.getMousePosXOnClick() / sizeCell)
        y:int = int(self.getMousePosYOnClick() / sizeCell)
        self.idx = y * gridWidth + x
        return self.idx

class Timer:
    _clock = None
    _dt:float = 0.016

    def __init__(self):
        self._clock = pygame.time.Clock()

    def update(self):
        self._dt = self._clock.tick(60)/1000

    def get_deltaTime(self):
        return self._dt
