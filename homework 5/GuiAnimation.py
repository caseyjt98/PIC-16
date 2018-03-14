#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:20:27 2018

@author: caseytaylor
"""

import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    
    
    def __init__(self):
        super(Example, self).__init__() # calls constructor for Parent class, QWidget      
        self.initUI() # call to construct subclass                  
        
    def initUI(self): 
        # diameter of ball, starting x pos, y pos
        self.d = 30; self.x = 0; self.y = 0; # starts top left corner    
        # speed in x diagonal direction, speed in y diagonal direction
        self.dx = 3; self. dy = 3;
        # box within ball can move (fill screen)
        self.boxwidth = 50; self.boxheight = 50;
        
        
        # create timer object
        self.timer = QtCore.QTimer()
        # connect timer to proper slot (self.animate)
        self.timer.timeout.connect(self.animate)
        # start animation immediately, calling self.animate every .005 seconds
        self.timer.start(5)  # start timer when initializing subclass of QWidget
        
        # set geometry of initial window 
        self.setGeometry(300,200,600,400)
        self.setWindowTitle('Animation')
        
        
        self.show()

    def paintEvent(self, e):
        # create QPainter object
        qp = QtGui.QPainter()
        
        # everything is done within begin, end
        qp.begin(self)
        
        # call drawRectangles, pass in QPainter object
        self.drawRectangles(qp)
        
        qp.end()
         
    def drawRectangles(self, qp):
        # set brush to white
        qp.setBrush(QtGui.QColor(255, 255, 255)) 
        # draw rectangle starting in top left corner
        qp.drawRect(0, 0, self.frameGeometry().width(), self.frameGeometry().height())
         
        # set color to red
        qp.setBrush(QtGui.QColor(255, 0, 0))
        # pass in characteristics of ball
        qp.drawEllipse(self.x, self.y, self.d, self.d)
 
      
    def animate(self):
        self.x += self.dx
        self.y += self.dy
        self.checkCollision()
        self.update() # requests that PaintEvent() be called
        
    
    def checkCollision(self):
        # if it hits wall of window 
        if (self.x <= 0) or ((self.x + self.d)>= self.width()): 
            self.dx = -self.dx # change direction
        if (self.y <= 0) or ((self.y + self.d)>= self.height()): 
            self.dy = -self.dy # change direction
              
def main():
    
    # create Application object
    app = QApplication([])
    # construct subclass
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()