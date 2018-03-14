#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:36:39 2018

@author: caseytaylor
"""

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QColorDialog
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QColor

class myWidget(QWidget):
    
    def __init__(self):
        super(myWidget,self).__init__()
        self.initUI()
        
    def initUI(self):
        # set side of square 
        self.side = 50; 
        
        # set default rectangle color to red
        self.rectColor = QtGui.QColor(255, 0, 0)
        
        # position of box
        self.x = 0; self.y = 0;

        # set geometry of initial window 
        self.setGeometry(300,200,600,400)
        
        # update every millisecond
        self.t = QTimer(self)
        self.t.timeout.connect(self.update)
        self.t.start(1)
        
        
        self.setWindowTitle('Click Drag')
        
        self.dragged = False
        self.pressed = False
        
        self.show()

    def paintEvent(self, e):
        
        # painter object
        painter = QtGui.QPainter()
        
        painter.begin(self)
        self.drawRectangles(painter)
        painter.end()

    
    def drawRectangles(self,painter):
        
        # draw white rectangle starting in top left corner, fill window screen
        painter.setBrush(QtGui.QColor(255, 255, 255)) 
        painter.drawRect(0, 0, self.frameGeometry().width(), self.frameGeometry().height())

        # draw red rectangle starting in top left corner
        painter.setBrush(self.rectColor)
        painter.drawRect(self.x, self.y, self.side, self.side)
            
    
    def mousePressEvent(self,e):
        self.pressed = True
        if e.x() >= self.x and e.x() <= (self.x + 50) and e.y() >= self.y and e.y() <= (self.y+50):
            self.dragged = True
            self.newX = e.x() - self.x
            self.newY = e.y() - self.y
    
    def mouseReleaseEvent(self,e):
        self.pressed = False
        self.dragged = False
    
    def mouseDoubleClickEvent(self,e): 
        # open color pallet
        if e.x() >= self.x and e.x() <= (self.x + 50) and e.y() >= self.y and e.y() <= (self.y+50):
            self.changeColor()
            
    def changeColor(self):
        self.colorDialog = QColorDialog(self)
        # set color
        self.rectColor = self.colorDialog.getColor()
        
     
    def mouseMoveEvent(self,e): # related to drag and drop motion
        # print e.x() # x coord of mouse click
        # print e.y() # y coord of mouse click
        
        # avoid jumping bug 
        if self.dragged == True:
            self.x = e.x() - self.newX
            self.y = e.y() - self.newY
        

def main():
    app = QApplication([])
    window = myWidget()
    app.exec_()
        
if __name__ == "__main__":
    main()