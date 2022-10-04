 #This Python file uses the following encoding: utf-8
#import sys
#from PySide6.QtWidgets import QApplication, QWidget, QPushButton
#from PySide6.QtCore import QTimer
#import pygame
#class Timer:
#    _clock = None
#    _dt:float = 0.016
#
#    def __init__(self):
#        self.clock = pygame.time.Clock()
#
#    def update(self):
#        self.dt = self.clock.tick(60)/1000
#
#    def get_deltaTime(self):
#        return self._dt
#
#class Window(QWidget):
#    def __init__(self,game):
#        super().__init__()
#        self.initUi()
#        self.init_pygame(game)
#
#    def init_pygame(self,game):
#        self.game = game
#        self.timer = QTimer()
#        self.timer.timeout.connect(self.pygame_loop)
#        self.timer.start(0)
#
#    def pygame_loop(self):
#        if self.game.loop():
#            self.close()
#
#    def initUi(self):
#        self.setWindowTitle("Interface Dames")
#        self.setGeometry(10,10,300,200) #grandeur de l'écran
#
#        self.button = QPushButton("Do not click",self)
#        self.button.setToolTip("Don't you dare !")
#        self.button.move(100,70)
#        self.button.clicked.connect(self.onClick)
#        self.show()
#        pass
#
#    def onClick(self):
#        pass
#
#class Game:
#    def __init__(self):
#        pygame.init()
#        self.timer = Timer()
#        self.gameInit()
#        self.shouldQuit() == False
#
#    def gameInit(self):
#           self.size = self.width, self.height = 640, 480
#           self.black = [0,0,0] #pas obligé de mettre les square brackets mais c'est beaucoup plus beau, n
#           self.screen = pygame.display.set_mode(self.size)
#
#    def render(self):
#            self.screen.fill(self.black)
#            self.screen.blit(self.maxime, self.maximerect)
#            pygame.display.flip() #equivalent au render present dans SDL
#
#    def processInput(self):
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                self.shouldQuit = True
#            if event.type == pygame.KEYDOWN:
#                if event.key == 119: #119 c'est W, 115 c'est S
#                    pass #entrer ce que la touche va faire
#            if event.type == pygame.KEYUP:
#                if event.key == 115:
#                    pass #entrer ce que la touche va fa
#    def loop(self):
#        self.timer.update()
#        dt = self.time.get_deltaTim
#        self.processInput()
#        #Update Actors
#        self.render()
#        return self.shou
#
#def main():
#    app = QApplication(sys.argv)
#    game = Game()
#    exe = Window(game)
#    app.setActiveWindow(exe)
#    sys.exit(app.exec())
#
#if __name__ == "__main__":
#    main()
#


import sys
import pygame

from Game import Game
from Window import Window
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QSlider
from PySide6.QtCore import QTimer

def main():
    app = QApplication(sys.argv)
    game = Game()
    exe = Window(game)
    app.setActiveWindow(exe)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()



#class Timer:
#    _clock = None
#    _dt:float = 0.016
#
#    def __init__(self):
#        self.clock = pygame.time.Clock()
#
#    def update(self):
#        self.dt = self.clock.tick(60)/1000
#
#    def get_deltaTime(self):
#        return self._dt
#
#class Game:
#    def __init__(self):
#        pygame.init()
#        self.timer = Timer()
#        self.gameInit()
#        self.shouldQuit = False
#        pass
#
#    def gameInit(self):
#        self.size = self.width, self.height = 640, 480
#        self.black = [0,0,0] #pas obligé de mettre les square brackets mais c'est beaucoup plus beau, non?
#
#        self.screen = pygame.display.set_mode(self.size)
#
#        #self.maxime = pygame.image.load("maxime.png")
#        #self.maximerect = self.maxime.get_rect()
#        #self.maximerect.x = self.maximerect.y = 0
#
#        self.circle = pygame.Surface([111,111])
#        self.circlerect = pygame.draw.circle(self.circle,pygame.Color(255,0,0),[self.circle.get_width()/2,self.circle.get_height()/2], 50)
#        pass
#
#    def render(self):
#        self.screen.fill(self.black)
#        #self.screen.blit(self.maxime, self.maximerect)
#        pygame.display.flip() #equivalent au render present dans SDL
#
#    def processInput(self):
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                self.shouldQuit = True
#            if event.type == pygame.KEYDOWN:
#                if event.key == 119: #119 c'est W, 115 c'est S
#                    pass #entrer ce que la touche va faire
#            if event.type == pygame.KEYUP:
#                if event.key == 115:
#                    pass #entrer ce que la touche va faire

#    def loop(self):
#        self.timer.update()
#        dt = self.timer.get_deltaTime()
#
#        self.processInput()
#        #Update Actors
#        self.render()
#        return self.shouldQuit
#
#class Window(QWidget):
#    def __init__(self,game):
#        super().__init__()
#        self.initUi()
#        self.init_pygame(game)
#
#    def init_pygame(self,game):
#        self.game = game
#        self.timer = QTimer()
#        self.timer.timeout.connect(self.pygame_loop)
#        self.timer.start(0)
#
#    def pygame_loop(self):
#        if self.game.loop():
#            self.close()
#
#    def initUi(self):
#        self.setWindowTitle("Dames")
#        self.setGeometry(10,10,300,200) #grandeur de l'écran
#
#        self.button = QPushButton("Bonjour",self)
#        #self.button.setToolTip("Don't you dare !")
#        self.button.move(100,70)
#        self.button.clicked.connect(self.onClick)
#
#        self.show()
#        pass
#
#    def onClick(self):
#        pass
#    def onSlider(self):
#        slider:QSlider = self.sender()
#        print(slider.value())
#        pass
#
#def Grid():


