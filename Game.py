# This Python file uses the following encoding: utf-8
import pygame

from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import QTimer
from pygame import Surface

from Cell import Cell
from Grid import Grid
from Pion import Pion

class Game:
    __grid:Grid
    __pionBlanc:Pion = []
    __pionNoir:Pion = []
    __pion:Pion = []
    __selectPionIdx = 1000
    __pionIdToMove = 1000
    __cellsNoirs:Cell = []
    __mousePos:int = [0,0]
    __mouseClick:bool = False
    __idx:int = 0
    __oldIdx:int = 0
    __screen:Surface
    def __init__(self):
        pygame.init()
        self.timer = Timer()
        self.gameInit()
        self.shouldQuit = False
        self.__grid = Grid(5, self.width, self.height)
        self.setCellsNoirs()
        self.initPions(5)

    def gameInit(self):
        self.size = self.width, self.height = 800, 800
        red = [255,0,0]
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill(red)

    def render(self):
        self.__grid.renderGrid(self.screen)
        for i in range(self.__pion.__len__()):
            self.__pion[i].renderPion(self.screen, self.__grid.cell[i].getSize())
        pygame.display.flip() #equivalent au render present dans SDL

    def loop(self):
        self.timer.update()
        dt = self.timer.get_deltaTime
        self.processInput()
        self.__grid.Update(self.getMouseClick(), self.getCellIdx(), self.getOldCellIdx())
        self.setMouseClick(False)
        self.updateStates()
        self.render()
        return self.shouldQuit

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.shouldQuit = True
            if event.type == pygame.MOUSEMOTION:
                self.setMousePos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.onClick()

    def setCellsNoirs(self):
        for i in range(self.__grid.getLength()):
            if self.__grid.cell[i].getColorId() == "black":
                cn = self.__grid.cell[i]
                self.__cellsNoirs.append(cn)

    def getCellsNoirs(self):
        return self.__listCellsNoirs

    def getPionsBlanc(self):
        cn = self.getCellsNoirs()
        for i in range(cn.__len__()):
            print(cn[i])

    def initPions(self, nbrPionsJoueur):
        idx = 0
        for i in range(nbrPionsJoueur): #initialisation des pions
            xNoir = self.__cellsNoirs[i].getX()
            yNoir = self.__cellsNoirs[i].getY()

            xBlanc = self.__cellsNoirs[self.__cellsNoirs.__len__()- 1 - i].getX()
            yBlanc = self.__cellsNoirs[self.__cellsNoirs.__len__()- 1 - i].getY()

            size = self.__cellsNoirs[i].getSize()
            color = (255,255,255)
            colorId = self.__cellsNoirs[i].getColorId()

            type = "pion"
            teamN = "noir"
            teamB = "blanc"
            imgNoir = "pionNoir.png"
            imgBlanc = "pionBlanc.png"

            pn:Pion = Pion(xNoir, yNoir, size, color, idx, colorId, self.width, self.height, imgNoir, type, teamN, self.__cellsNoirs[i].getIdx())
            idx += 1
            pb:Pion = Pion(xBlanc, yBlanc, size, color, idx, colorId, self.width, self.height, imgBlanc, type, teamB, self.__cellsNoirs[self.__cellsNoirs.__len__()- 1 - i].getIdx())
            idx += 1
            self.__pion.append(pn)
            self.__pion.append(pb)

    def setMousePos(self):
        self.mousePos = pygame.mouse.get_pos()

    def onClick(self):
        self.setMouseClick(True)
        self.setOldCellIdx()
        self.setCellIdx()

    def setMouseClick(self, b):
        self.__mouseClick = b

    def getMouseClick(self):
        return self.__mouseClick

    def getMousePosX(self):
        return self.mousePos[0]

    def getMousePosY(self):
        return self.mousePos[1]

    def setCellIdx(self):
        sizeCell = self.__grid.cell[0].getSize()
        gridWidth:int = self.__grid.getWidth()
        x:int = int(self.getMousePosX() / sizeCell)
        y:int = int(self.getMousePosY() / sizeCell)
        self.__idx = y * gridWidth + x

    def getCellIdx(self):
        return self.__idx

    def setOldCellIdx(self):
        self.__oldIdx = self.getCellIdx()

    def getOldCellIdx(self):
        return self.__oldIdx

    def checkSelectedPion(self):
        for i in range(self.__pion.__len__()):
            #print(i,self.__pion[i].getIsSelected())
            for j in range(self.__cellsNoirs.__len__()):
                if self.__pion[i].getGridPosition() == self.__cellsNoirs[j].getIdx() and self.__cellsNoirs[j].getIsClicked() == True and self.__cellsNoirs[j].getIsOccupiedBy() == "blanc":
                    self.__pion[i].setIsSelected(True)
                    self.__selectPionIdx = self.__pion[i].getIdx()
                    #self.setSelectedPion(self.__pion[i].getGridPosition())
                elif self.__pion[i].getGridPosition() == self.__cellsNoirs[j].getIdx() and self.__cellsNoirs[j].getIsClicked() == False and self.__cellsNoirs[j].getIsOccupiedBy() == "blanc":
                    self.__pion[i].setIsSelected(False)

    #def setSelectedPion(self, pos):
    #    self.__selectPionPos = pos

    #def getSelectedPion(self):
    #    return self.__selectPionPos

    def setOccupiedGridCells(self):
        for i in range(self.__pion.__len__()):
            for j in range(self.__cellsNoirs.__len__()):
                if self.__pion[i].getGridPosition() == self.__cellsNoirs[j].getIdx():
                    self.__cellsNoirs[j].setIsOccupied(True)
                    if self.__pion[i].getTeam() == "blanc":
                        self.__cellsNoirs[j].setIsOccupiedBy("blanc")
                    elif self.__pion[i].getTeam() == "noir":
                        self.__cellsNoirs[j].setIsOccupiedBy("noir")

    def updatePionsState(self):
        self.checkSelectedPion()
        self.movePlayerPion()

    def updateCellsState(self):
        self.setOccupiedGridCells()
        #for i in range(self.__grid.cell.__len__()):
        #    print(i, self.__grid.cell[i].getIsOccupiedBy())

    def updateStates(self):
        self.updatePionsState()
        self.updateCellsState()

    def movePlayerPion(self):
        for i in range(self.__pion.__len__()):
            if self.__pion[i].getIsSelected() == True:
                self.__pionIdToMove = i
        if self.__pionIdToMove != 1000:
            for j in range(self.__grid.cell.__len__()):
                if self.__grid.cell[j].getIsClicked() == True and self.__grid.cell[j].getIsOccupied() == False:
                    self.__pion[self.__pionIdToMove].Move(self.__grid.cell[j].getX(), self.__grid.cell[j].getY())
                    self.__pion[self.__pionIdToMove].setGridPosition(j)
                    self.__pion[self.__pionIdToMove].setIsSelected(False)

                    self.__grid.cell[self.__oldIdx].setIsOccupied(False)
                    self.__grid.cell[self.__oldIdx].setIsOccupiedBy("none")
                    self.__grid.cell[j].setIsClicked(False)

                    self.__pionIdToMove = 1000
                    break



        #for i in range(self.__cellsNoirs.__len__()):
        #    #print('curr',self.__selectPionPos)
        #    #print(self.__grid.cell[i].getIdx())
        #    if self.__selectPionPos == self.__pion[i].getGridPosition():
        #        self.__pion[].Move(0,0)



class Timer:
    _clock = None
    _dt:float = 0.016

    def __init__(self):
        self._clock = pygame.time.Clock()

    def update(self):
        self._dt = self._clock.tick(60)/1000

    def get_deltaTime(self):
        return self._dt




    #def initOccupiedGridCells(self):
    #    for i in range(self.__pion.__len__()):
    #        for j in range(self.__cellsNoirs.__len__()):
    #            if self.__pion[i].getGridPosition() == self.__cellsNoirs[j].getIdx():
    #                self.__cellsNoirs[j].setIsOccupied(True)
    #                if self.__pion[i].getTeam() == "blanc":
    #                    self.__cellsNoirs[j].setIsOccupiedBy("blanc")
    #                elif self.__pion[i].getTeam() == "noir":
    #                    self.__cellsNoirs[j].setIsOccupiedBy("noir")
        #for j in range(self.__grid.cell.__len__()):
        #    print(self.__grid.cell[j].getIsOccupiedBy())


        #def setPionIdxPosition(self):
        #    sizePion = self.__pion[0].getSize()
        #    print(sizePion)




        #for j in range(self.__grid.cell.__len__()):
        #    print(self.__grid.cell[j].getIsOccupiedBy())


        #for i in range(self.__cellsNoirs.__len__()):
        #    for j in range(self.__pion.__len__()):
        #        if self.__cellsNoirs[i].getIdx() == self.__pion[j].getGridPosition():
        #            self.__cellsNoirs[j].setIsOccupied(True)
        #for i in range(self.__grid.cell.__len__()):
            #print('cell:' ,i,',',self.__grid.cell[i].getIsOccupied())

            #if
            #self.__grid.cell[j].setIsOccupied(True)
            #print(self.__grid.cell[j].getIdx())

    #def initPionsByTeam(self):
    #    pionListLen = self.__pion.__len__()
    #    idxW = 0
    #    idxB = 0
    #    for i in range(pionListLen):
    #        p:Pion = self.__pion[i]
    #        if self.__pion[i].getTeam() == "blanc":
    #            self.__pionBlanc.append(p)
    #            self.__pionBlanc[idxW].setIdx(i)
    #            idxW += 1
#
    #        if self.__pion[i].getTeam() == "noir":
    #            self.__pionNoir.append(p)
    #            self.__pionNoir[idxB].setIdx(i)
    #            idxB += 1
