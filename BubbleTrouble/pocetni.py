import sys

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow

from key_notifier import KeyNotifier
from ballMovement import BallMovement
from hitBall import HitBall
from arrowMovement import ArrowMovement


class SimMoveDemo(QMainWindow):

    def __init__(self):
        super().__init__()

        pix11 = QPixmap('player.png')
        pix22 = QPixmap('player2.png')
        # pix33 = QPixmap('arrow.png')
        # pix44 = QPixmap('arrow.png')
        pix55 = QPixmap('ball.png')

        self.label3 = QLabel(self)
        self.label4 = QLabel(self)
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label5 = QLabel(self)
        self.label6 = QLabel(self)
        self.labelispis = QLabel(self)
        self.labelispis2 = QLabel(self)

        self.timerP1 = QTimer(self)
        self.timerP1.setInterval(2000)
        self.timerP1.setSingleShot(True)

        self.timerP2 = QTimer(self)
        self.timerP2.setInterval(2000)
        self.timerP2.setSingleShot(True)

        oImage = QImage("fantasy_border.png")

        self.hitFloor = False
        self.hitSide = False

        self.arr1h = 10
        self.arr2h = 10

        self.arr1hidden = True
        self.arr2hidden = True

        self.pix1 = pix11.scaledToHeight(84)
        self.pix1 = pix11.scaledToWidth(34)

        self.pix2 = pix22.scaledToHeight(204)
        self.pix2 = pix22.scaledToWidth(34)

        self.pix5 = pix55.scaledToHeight(384)
        self.pix5 = pix55.scaledToWidth(54)

        # self.pix3 = pix33.scaledToHeight(200)
        # self.pix3 = pix33.scaledToWidth(5)
        # self.pix4 = pix44.scaledToHeight(200)
        # self.pix4 = pix44.scaledToWidth(5)

        palette = QPalette()
        sImage = oImage.scaled(QSize(1920, 1080))
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.setWindowState(Qt.WindowFullScreen)
        self.__init_ui__()

        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

        self.ballMovement = BallMovement()
        self.ballMovement.ballMovementSignal.connect(self.moveBall)
        self.ballMovement.start()

    def __init_ui__(self):
        font = QtGui.QFont()
        font.setPointSize(40)

        self.labelispis.setFont(font)
        self.labelispis.resize(100000, 100)
        self.labelispis.setGeometry(1500, 940, 400, 200)

        self.labelispis2.setFont(font)
        self.labelispis2.resize(100000, 100)
        self.labelispis2.setGeometry(0, 940, 400, 200)

        self.label1.setPixmap(self.pix1)
        self.label1.setGeometry(1000, 900, 50, 50)

        self.label2.setPixmap(self.pix2)
        self.label2.setGeometry(900, 900, 50, 50)

        self.label5.setPixmap(self.pix5)
        self.label5.setGeometry(50, 50, 50, 50)

        self.label3.resize(8, 950)
        pixmap1 = QtGui.QPixmap('arrow.png')
        self.pixmap = pixmap1.scaled(8, 950)
        self.label3.setPixmap(self.pixmap)
        self.label3.hide()

        self.label4.resize(8, 950)
        pixmap1 = QtGui.QPixmap('arrow.png')
        self.pixmap = pixmap1.scaled(8, 950)
        self.label4.setPixmap(self.pixmap)
        self.label4.hide()

        self.label6.resize(1920, 100)
        pixmap1 = QtGui.QPixmap('ScoreBackground.jpg')
        self.pixmapScore = pixmap1.scaled(1920, 150)
        self.label6.setPixmap(self.pixmapScore)
        self.label6.setGeometry(0, 950, 1920, 145)

        x = 'Player1:'
        y = 'Player2:'
        score1 = 10000
        score2 = 50000

        self.statusBar().setFont(font)
        self.labelispis.setText(str(x) + str(score1))
        self.labelispis2.setText(str(y) + str(score2))
        self.setWindowTitle('BubbleTrouble')

        self.show()

    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())

    def __update_position__(self, key):
        rec1 = self.label1.geometry()
        rec2 = self.label2.geometry()
        #rec3 = self.label3.geometry()
        #rec4 = self.label4.geometry()

        if key == Qt.Key_Right:
            if rec1.x() < 1880:
                self.label1.setGeometry(rec1.x() + 15, rec1.y(), rec1.width(), rec1.height())
        elif key == Qt.Key_Up:
            if self.arr1hidden:
                geometrija = self.label1.geometry()
                broj1 = geometrija.x()
                broj2 = geometrija.y()
                self.arrowMovement = ArrowMovement()
                self.arrowMovement.add_list(broj1)
                self.arrowMovement.add_list(broj2)
                self.arrowMovement.ballX = broj1
                self.arrowMovement.arrowMovementSignal.connect(self.arrowMove)
                self.arrowMovement.start()
        elif key == Qt.Key_Left:
            if rec1.x() > 15:
                self.label1.setGeometry(rec1.x() - 15, rec1.y(), rec1.width(), rec1.height())
        if key == Qt.Key_D:
            if rec2.x() < 1880:
                self.label2.setGeometry(rec2.x() + 15, rec2.y(), rec2.width(), rec2.height())
        elif key == Qt.Key_W:
            if self.arr2hidden:
                geometrija = self.label2.geometry()
                broj1 = geometrija.x()
                broj2 = geometrija.y()
                self.arrowMovement2 = ArrowMovement()
                self.arrowMovement2.add_list(broj1)
                self.arrowMovement2.add_list(broj2)
                self.arrowMovement2.ballX = broj1
                self.arrowMovement2.arrowMovementSignal.connect(self.arrowMove2)
                self.arrowMovement2.start()
        elif key == Qt.Key_A:
            if rec2.x() > 15:
                self.label2.setGeometry(rec2.x() - 15, rec2.y(), rec2.width(), rec2.height())

    def moveBall(self):
        rec5 = self.label5.geometry()
        if (rec5.y() == 900):
            self.hitFloor = True
        elif (rec5.y() == 0):
            self.hitFloor = False
        if (rec5.x() == 1880):
            self.hitSide = True
        elif (rec5.x() == 0):
            self.hitSide = False

        if self.hitSide and not self.hitFloor:
            self.label5.setGeometry(rec5.x() - 10, rec5.y() + 10, rec5.width(), rec5.height())
        elif not self.hitSide and self.hitFloor:
            self.label5.setGeometry(rec5.x() + 10, rec5.y() - 10, rec5.width(), rec5.height())
        elif not self.hitFloor and not self.hitSide:
            self.label5.setGeometry(rec5.x() + 10, rec5.y() + 10, rec5.width(), rec5.height())
        elif self.hitSide and self.hitFloor:
            self.label5.setGeometry(rec5.x() - 10, rec5.y() - 10, rec5.width(), rec5.height())

    def arrowMove(self, lista):
        self.arr1hidden = False
        rec3 = self.label3.geometry()
        rec1 = self.label1.geometry()
        self.label3.show()

        broj1 = lista[0]
        broj2 = lista[1]
        if (self.arr1h != 900):
            self.arr1h += 10
            self.label3.setGeometry(broj1 + 15, broj2 - self.arr1h, rec3.width(), rec3.height())
            self.hitBall = HitBall()
            self.hitBall.hitBallSignal.connect(self.checkHit)
            self.hitBall.start()

        else:
            self.hideArrow1()
            self.arrowMovement.ballX = None

    def arrowMove2(self, lista):
        self.arr2hidden = False
        rec3 = self.label4.geometry()
        rec1 = self.label2.geometry()
        self.label4.show()

        broj1 = lista[0]
        broj2 = lista[1]
        if (self.arr2h != 900):
            self.arr2h += 10
            self.label4.setGeometry(broj1 + 15, broj2 - self.arr2h, rec3.width(), rec3.height())
            self.hitBall2 = HitBall()
            self.hitBall2.hitBallSignal.connect(self.checkHit2)
            self.hitBall2.start()
        else:
            self.hideArrow2()
            self.arrowMovement2.ballX = None

    def closeEvent(self, event):
        self.key_notifier.die()

    def hideArrow2(self):
        self.label4.hide()
        self.arr2h = 10
        self.arr2hidden = True
        self.arrowMovement2.die()

    def hideArrow1(self):
        self.label3.hide()
        self.arr1h = 10
        self.arr1hidden = True
        self.arrowMovement.die()

    def checkHit(self):
        ballPosition = self.label5.geometry()

        if ballPosition.x() == self.arrowMovement.ballX:
            self.label5.hide()
            self.ballMovement.is_done = True

    def checkHit2(self):
        ballPosition = self.label5.geometry()

        if ballPosition.x() == self.arrowMovement2.ballX:
            self.label5.hide()
            self.ballMovement.is_done = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimMoveDemo()
    sys.exit(app.exec_())
