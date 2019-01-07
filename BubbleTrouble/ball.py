from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ball(QLabel):
    def __init__(self, slika, velicina, x, y, parent=None):
        QLabel.__init__(self, parent)

        self.slika = QPixmap(slika)
        self.velicina = velicina
        self.labelBall = QLabel(self)
        self.pix5 = self.slika.scaledToHeight(x)
        self.pix5 = self.slika.scaledToWidth(y)
        self.labelBall.setPixmap(self.pix5)
        self.labelBall.setGeometry(x,y,x,y)
        self.hitFloor = False
        self.hitSide = False

    def __init_ui__(self):
        self.labelBall.show()

    def showBall(self):
        self.labelBall.show();

    def pogodjena(self):
        if self.velicina > 1:
            self.velicina -= 1

    def setSize(self, xx, yy):
        self.labelBall.resize(xx, yy)

    def moveBall(self):
        #self.labelBall.move(1000, -200)
        rec5 = self.labelBall.geometry()

        """"
        if (rec5.y() == 420):
            self.hitFloor = True
        elif (rec5.y() == -450):
            self.hitFloor = False
        if (rec5.x() == 1880):
            self.hitSide = True
        elif (rec5.x() == 0):
            self.hitSide = False
        """
        if (rec5.y() == 900):
            self.hitFloor = True
        elif (rec5.y() == 0):
            self.hitFloor = False
        if (rec5.x() == 1880):
            self.hitSide = True
        elif (rec5.x() == 0):
            self.hitSide = False

        if self.hitSide and not self.hitFloor:
            self.labelBall.setGeometry(rec5.x() - 10, rec5.y() + 10, rec5.width(), rec5.height())
        elif not self.hitSide and self.hitFloor:
            self.labelBall.setGeometry(rec5.x() + 10, rec5.y() - 10, rec5.width(), rec5.height())
        elif not self.hitFloor and not self.hitSide:
            self.labelBall.setGeometry(rec5.x() + 10, rec5.y() + 10, rec5.width(), rec5.height())
        elif self.hitSide and self.hitFloor:
            self.labelBall.setGeometry(rec5.x() - 10, rec5.y() - 10, rec5.width(), rec5.height())
