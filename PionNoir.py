# This Python file uses the following encoding: utf-8
import pygame
from Pion import Pion
from pygame import Surface

class PionNoir(Pion):
    def __init__(self, x, y ,size, color, screenW, screenH, image:str):
        super().__init__(self, x, y ,size, color, screenW, screenH, image)



#class PionNoir(Pion):
#    pion:Pion = []
#    def __init__(self,x, y, size, color, screenW, screenH, image):
#        super().init(x, y, size, color, screenW, screenH)
#        self.initPionNoir(x, y, size, color, screenW, screenH, image)
#
#    def initPionNoir(self, x, y, size, color, screenW, screenH, image):
#        for i in range(0, 12):
#            x = 0
#            y = 0
#            size = size
#            color = color
#            p:Pion = Pion(x, y, size, color, screenW, screenH, image)
#            self.pion.append(p)
#
#    def renderPionNoir(self, screen:Surface):
#        for p in self.pion:
#            pion:Pion = p
#            pion.render(screen)
#
