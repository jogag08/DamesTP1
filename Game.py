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
    __selectPion = None
    __pionIdToMove = 1000
    __mousePos:int = [0,0]
    __mouseClick:bool = False
    __idx:int = 0
    __oldIdx:int = 0
    __screen:Surface
    __dictio = {}
    __possibleMoves:int = []
    __isLoaded:bool = False
    def __init__(self):
        pygame.init()
        self.timer = Timer()
        self.gameInit()
        self.shouldQuit = False
        self.__grid = Grid(5, self.width, self.height)
        self.initPions(5)
        self.setDictio()

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
        self.TEST()
        self.setMouseClick(False)
        self.updateStates()
        self.setDictio()
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

    def initPions(self, nbrPionsJoueur):
        idx = 0
        type = "pion"
        teamN = "noir"
        teamB = "blanc"
        imgNoir = "pionNoir.png"
        imgBlanc = "pionBlanc.png"
        color = (255,255,255)
        idx = 0
        for i in range(nbrPionsJoueur*2): #initialisation des pions blancs
            if self.__grid.cell[self.__grid.cell.__len__() - 1 - i].getColorId() == "noir":
                self.__grid.cell[self.__grid.cell.__len__() - 1 - i].setDictId(1)
                x = self.__grid.cell[self.__grid.cell.__len__() - 1 - i].getX()
                y = self.__grid.cell[self.__grid.cell.__len__() - 1 - i].getY()
                size = self.__grid.cell[i].getSize()
                colorId = self.__grid.cell[i].getColorId()
                p:Pion = Pion(x, y, size, color, idx, colorId, self.width, self.height, imgBlanc, type, teamB, self.__grid.cell[self.__grid.cell.__len__() - 1 - i].getIdx())
                idx += 1
                self.__pion.append(p)
        idx -= 1
        for i in range(nbrPionsJoueur*2): #initalisation de pions noirs
            if self.__grid.cell[i].getColorId() == "noir":
                self.__grid.cell[i].setDictId(3)
                x = self.__grid.cell[i].getX()
                y = self.__grid.cell[i].getY()
                size = self.__grid.cell[i].getSize()
                colorId = self.__grid.cell[i].getColorId()
                p:Pion = Pion(x, y, size, color, idx, colorId, self.width, self.height, imgNoir, type, teamN, self.__grid.cell[i].getIdx())
                idx += 1
                self.__pion.append(p)

    def setDictio(self):
        for i in range(self.__grid.cell.__len__()):
            self.__dictio[i] = str(self.__grid.cell[i].getDictId())
            print(self.__dictio)

    def setMousePos(self):
        self.mousePos = pygame.mouse.get_pos()

    def onClick(self):
        self.setMouseClick(True)
        self.setOldCellIdx()
        self.setCellIdx()
        self.__isLoaded = False

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
        test = y * gridWidth + x
        if self.__grid.cell[test].getColorId() == "noir":
            self.__idx = test
        elif self.__grid.cell[test].getColorId() == "blanc":
            self.__idx = self.__idx

    def getCellIdx(self):
        return self.__idx

    def setOldCellIdx(self):
        self.__oldIdx = self.getCellIdx()

    def getOldCellIdx(self):
        return self.__oldIdx

    def checkSelectedPion(self):
        for i in range(self.__pion.__len__()):
            for j in range(self.__grid.cell.__len__()):
                if self.__grid.cell[j].getIsClicked() == True and self.__pion[i].getGridPosition() == self.__grid.cell[j].getIdx():
                    self.__pion[i].setIsSelected(True)
                    self.__selectPion = self.__pion[i]
                elif self.__grid.cell[j].getIsClicked() == False and self.__pion[i].getGridPosition() == self.__grid.cell[j].getIdx():
                    self.__pion[i].setIsSelected(False)

    def setOccupiedGridCells(self):
        for i in range(self.__pion.__len__()):
            if (self.__pion[i].getIsAlive() == True):
                for j in range(self.__grid.cell.__len__()):
                    if self.__pion[i].getGridPosition() == self.__grid.cell[j].getIdx():
                        if self.__pion[i].getTeam() == "blanc":
                            self.__grid.cell[j].setIsOccupiedBy("blanc")
                        elif self.__pion[i].getTeam() == "noir":
                            self.__grid.cell[j].setIsOccupiedBy("noir")
                        else:
                            self.__grid.cell[j].setIsOccupiedBy("none")
            if (self.__pion[i].getIsAlive() == False):
                for j in range(self.__grid.cell.__len__()):
                     self.__grid.cell[j].setIsOccupiedBy("none")

    def setClickedCell(self):
        for i in range(self.__grid.cell.__len__()):
            if (self.__idx == self.__grid.cell[i].getIdx()) and self.__grid.cell[i].getColorId() == "noir":
                self.__grid.cell[i].setIsClicked(True)
                self.setSelectHighLight(self.__grid.cell[i])
            elif self.__idx == 0 and self.__grid.cell[i].getColorId() == "noir" and self.__grid.cell[i].getIsOccupiedBy() == "noir":
                for k in range(self.__pion.__len__()):
                    self.__pion[k].setIsSelected(False)
            else:
                self.__grid.cell[i].setIsClicked(False)
                self.setSelectHighLight(self.__grid.cell[i])

    def setSelectHighLight(self,c):
        originalColor = (110, 0, 0)
        if c.getIsClicked() == True and c.getColorId() == "noir":
            c.setColor([240,60,30])
        if c.getIsClicked() == False and c.getColorId() == "noir":
            c.setColor(originalColor)

    def checkPionType(self):
        for i in range(self.__pion.__len__()):
            if self.__pion[i].getTeam() == "blanc":
                self.__pion[i].getGridPosition()
                if self.__pion[i].getType() =="pion" and self.__pion[i].getGridPosition() == 1 or self.__pion[i].getGridPosition() == 3:
                    self.__pion[i].setType("reine")
                    self.__pion[i].setPionImage("reineBlanc.png")
            if self.__pion[i].getTeam() == "noir":
                self.__pion[i].getGridPosition()
                if self.__pion[i].getType() =="pion" and self.__pion[i].getGridPosition() == 21 or self.__pion[i].getGridPosition() == 23:
                    self.__pion[i].setType("reine")
                    self.__pion[i].setPionImage("reineNoir.png")

    def checkPossibleMoves(self):
        for i in range(self.__pion.__len__()):
            if self.__pion[i].getIsSelected() == True and self.__isLoaded == False and self.__pion[i].getGridPosition() == self.__idx:
                print(self.__pion[i].getGridPosition())
                self.__possibleMoves.clear()
                #--------------------------Déplacements possibles pour les positions 7, 11, 13, 17
                if self.__pion[i].getGridPosition() == 7 or self.__pion[i].getGridPosition() == 17 or self.__pion[i].getGridPosition() == 11 or self.__pion[i].getGridPosition() == 13:
                    if self.__pion[i].getType() == "pion":
                        if self.__pion[i].getTeam() == "blanc":
                            pm1 = self.__pion[i].getGridPosition() - 4
                            pm2 = self.__pion[i].getGridPosition() - 6
                            self.__possibleMoves.append(pm1)
                            self.__possibleMoves.append(pm2)
                        if self.__pion[i].getTeam() == "noir":
                            pm1 = self.__pion[i].getGridPosition() + 4
                            pm2 = self.__pion[i].getGridPosition() + 6
                            self.__possibleMoves.append(pm1)
                            self.__possibleMoves.append(pm2)
                    elif self.__pion[i].getType() == "reine":
                        pm1 = self.__pion[i].getGridPosition() - 4
                        pm2 = self.__pion[i].getGridPosition() - 6
                        pm3 = self.__pion[i].getGridPosition() + 4
                        pm4 = self.__pion[i].getGridPosition() + 6
                        self.__possibleMoves.append(pm1)
                        self.__possibleMoves.append(pm2)
                        self.__possibleMoves.append(pm3)
                        self.__possibleMoves.append(pm4)

                #--------------------------Déplacements possibles pour les positions 5, 15
                if self.__pion[i].getGridPosition() == 5 or self.__pion[i].getGridPosition() == 15:
                    if self.__pion[i].getType() == "pion":
                        if self.__pion[i].getTeam() == "blanc":
                            pm1 = self.__pion[i].getGridPosition() - 4
                            self.__possibleMoves.append(pm1)
                        if self.__pion[i].getTeam() == "noir":
                            pm1 = self.__pion[i].getGridPosition() + 6
                            self.__possibleMoves.append(pm1)
                    elif self.__pion[i].getType() == "reine":
                        pm1 = self.__pion[i].getGridPosition() - 4
                        pm2 = self.__pion[i].getGridPosition() + 6
                        self.__possibleMoves.append(pm1)
                        self.__possibleMoves.append(pm2)

                #--------------------------Déplacements possibles pour les positions 9, 19
                if self.__pion[i].getGridPosition() == 9 or self.__pion[i].getGridPosition() == 19:
                    if self.__pion[i].getType() == "pion":
                        if self.__pion[i].getTeam() == "blanc":
                            pm1 = self.__pion[i].getGridPosition() - 6
                            self.__possibleMoves.append(pm1)
                        if self.__pion[i].getTeam() == "noir":
                            pm1 = self.__pion[i].getGridPosition() + 4
                            self.__possibleMoves.append(pm1)
                    elif self.__pion[i].getType() == "reine":
                        pm1 = self.__pion[i].getGridPosition() + 4
                        pm2 = self.__pion[i].getGridPosition() - 6
                        self.__possibleMoves.append(pm1)
                        self.__possibleMoves.append(pm2)

                #--------------------------Déplacements possibles pour les positions 1, 3
                if self.__pion[i].getGridPosition() == 21 or self.__pion[i].getGridPosition() == 23:
                    pm1 = self.__pion[i].getGridPosition() - 4
                    pm2 = self.__pion[i].getGridPosition() - 6
                    self.__possibleMoves.append(pm1)
                    self.__possibleMoves.append(pm2)

                #--------------------------Déplacements possibles pour les positions 21, 23
                if self.__pion[i].getGridPosition() == 1 or self.__pion[i].getGridPosition() == 3:
                    pm1 = self.__pion[i].getGridPosition() + 4
                    pm2 = self.__pion[i].getGridPosition() + 6
                    self.__possibleMoves.append(pm1)
                    self.__possibleMoves.append(pm2)
                self.__isLoaded = True


    #def checkPossibleKills(self):
    #    for i in range(self.__possibleMoves.__len__()):
    #        for i in range(self.__grid.cell.__len__()):
    #            if self.__possibleMoves[i] == self.grid.cell[k].getIdx() and self.grid.cell[k].getIsOccupiedBy() != "none"
    #            #--------------------------Kills possibles pour la position 1
    #                if self.__pion[i].getGridPosition() == 1 or self.__pion[i].getGridPosition() == 17 or self.__pion[i].getGridPosition() == 11 or self.__pion[i].getGridPosition() == 13:
    #                    if self.__pion[i].getType() == "pion":
    #                        if self.__pion[i].getTeam() == "blanc":
    #                            pm1 = self.__pion[i].getGridPosition() - 4
    #                            pm2 = self.__pion[i].getGridPosition() - 6
    #                            self.__possibleMoves.append(pm1)
    #                            self.__possibleMoves.append(pm2)
    #                        if self.__pion[i].getTeam() == "noir":
    #                            pm1 = self.__pion[i].getGridPosition() + 4
    #                            pm2 = self.__pion[i].getGridPosition() + 6
    #                            self.__possibleMoves.append(pm1)
    #                            self.__possibleMoves.append(pm2)
    #                    elif self.__pion[i].getType() == "reine":
    #                        pm1 = self.__pion[i].getGridPosition() - 4
    #                        pm2 = self.__pion[i].getGridPosition() - 6
    #                        pm3 = self.__pion[i].getGridPosition() + 4
    #                        pm4 = self.__pion[i].getGridPosition() + 6
    #                        self.__possibleMoves.append(pm1)
    #                        self.__possibleMoves.append(pm2)
    #                        self.__possibleMoves.append(pm3)
    #                        self.__possibleMoves.append(pm4)

    def TEST(self):
        pass
        #print(self.__isLoaded)
        #print(self.__possibleMoves)
        #print(self.__selectPion)
        #for i in range(self.__grid.cell.__len__()):
        #    print(i,self.__grid.cell[i].getIsClicked())
        #    print(i,self.__grid.cell[i].getColorId())
        #    print(i, self.__idx)
        #    #print(i, self.__grid.cell[i].getIsOccupiedBy())

    def updatePionsState(self):
        self.checkSelectedPion()
        self.movePlayerPion()
        self.checkPossibleMoves()
        self.checkPionType()

    def updateCellsState(self):
        self.setClickedCell()
        self.setOccupiedGridCells()
        self.setDictio()

    def updateStates(self):
        self.updatePionsState()
        self.updateCellsState()

    def movePlayerPion(self):
        for i in range(self.__pion.__len__()):
            if self.__pion[i].getIsSelected() == True:
                self.__pionIdToMove = i
        if self.__pionIdToMove != 1000:
            for j in range(self.__grid.cell.__len__()):
                for k in range(self.__possibleMoves.__len__()):
                    if self.__grid.cell[j].getIsClicked() == True and (self.__grid.cell[j].getIsOccupiedBy() == "none") and self.__grid.cell[j].getIdx() == self.__possibleMoves[k]:
                        self.__pion[self.__pionIdToMove].Move(self.__grid.cell[j].getX(), self.__grid.cell[j].getY())
                        self.__pion[self.__pionIdToMove].setGridPosition(j)
                        self.__pion[self.__pionIdToMove].setIsSelected(False)
                        self.__grid.cell[self.__oldIdx].setIsOccupiedBy("none")
                        self.__grid.cell[self.__oldIdx].setIsClicked(False)
                        self.__pionIdToMove = 1000
                        self.__idx = 0
                        self.__possibleMoves.clear()
                        self.__isLoaded = False

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
