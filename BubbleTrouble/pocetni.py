import sys

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow, QVBoxLayout

from key_notifier import KeyNotifier
from ballMovement import BallMovement
from hitBall import HitBall
from arrowMovement import ArrowMovement
from ball import Ball
from addBall import AddBall
bolian = False
class SimMoveDemo(QMainWindow):

    def __init__(self):
        super().__init__()

        pix11 = QPixmap('player.png')
        pix22 = QPixmap('player2.png')
        # pix33 = QPixmap('arrow.png')
        # pix44 = QPixmap('arrow.png')
        pix55 = QPixmap('ball.png')
        pix66 = QPixmap('bal2.png')
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label5 = QLabel(self)
        self.label6 = QLabel(self)
        self.labe21 = QLabel(self)
        self.labe211 = QLabel(self)
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

        self.hitFloor2 = False
        self.hitSide2 = False
        self.da = False
        self.hitFloor3 = False
        self.hitSide3 = False

        self.hitFloor4 = False
        self.hitSide4 = False

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
        self.pix6 = pix66.scaledToHeight(384)
        self.pix6 = pix66.scaledToWidth(54)
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

        self.bol = False
        self.bol2 = False
        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

        self.ballMovement = BallMovement()
        self.ballMovement.ballMovementSignal.connect(self.moveBall)
        self.ballMovement.start()

        self.ballMovement3 = BallMovement()
        self.ballMovement3.ballMovementSignal.connect(self.moveBall3)
        self.ballMovement3.start()

        self.ballMovement4 = BallMovement()
        self.ballMovement4.ballMovementSignal.connect(self.moveBall4)
        self.ballMovement4.start()
        #self.v = QVBoxLayout()
        self.loptaKlasa = Ball('ball.png', 2, 30, 30)
        self.AddBall = AddBall()
        self.AddBall.add_ball(self.loptaKlasa)
        self.AddBall.ball_signal.connect(self.postaviLoptu)
        self.ballMovement2 = BallMovement()
        self.ballMovement2.ballMovementSignal.connect(self.loptaKlasa.moveBall)

    def __init_ui__(self):
        font = QtGui.QFont()
        font.setPointSize(40)

        """"    OVO je za sad jedini nacin da se lopta pojavila 
        self.lopta = QLabel(self)
        Lopta = Ball('ball.png', 2, 100, 100)
        Lopta.setSize(80, 80)
        #self.lopta.showBall()
        self.lopta = Lopta.labelBall
        self.setCentralWidget(Lopta.labelBall)
        
        KORDINATE KRETANJA LOPTE TREBA POPRAVITI
        """

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

        self.labe21.setPixmap(self.pix6)
        self.labe21.setGeometry(50, 50, 50, 50)
        self.labe21.hide()
        self.labe211.setPixmap(self.pix6)
        self.labe211.setGeometry(50, 50, 50, 50)
        self.labe211.hide()
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
        score1 = 1000
        score2 = 5000

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

    def moveBall3(self):
        rec9 = self.labe21.geometry()
        if (rec9.y() > 900):
            self.hitFloor2 = True
        elif (rec9.y() == 0):
            self.hitFloor2 = False
        if (rec9.x() == 1880):
            self.hitSide2 = True
        elif (rec9.x() == 0):
            self.hitSide2 = False

        if self.hitSide2 and not self.hitFloor2:
            self.labe21.setGeometry(rec9.x() - 10, rec9.y() + 10, rec9.width(), rec9.height())
        elif not self.hitSide2 and self.hitFloor2:
            self.labe21.setGeometry(rec9.x() + 10, rec9.y() - 10, rec9.width(), rec9.height())
        elif not self.hitFloor2 and not self.hitSide2:
            self.labe21.setGeometry(rec9.x() + 10, rec9.y() + 10, rec9.width(), rec9.height())
        elif self.hitSide2 and self.hitFloor2:
            self.labe21.setGeometry(rec9.x() - 10, rec9.y() - 10, rec9.width(), rec9.height())

    def moveBall4(self):
        rec6 = self.labe211.geometry()

        if (rec6.y() >= 900):
            self.hitFloor3 = True
        elif (rec6.y() <= 0):
            self.hitFloor3 = False
        if (rec6.x() >= 1880):
            self.hitSide3 = False
        elif (rec6.x() <= 0):
            self.hitSide3 = True

        if self.hitSide3 and not self.hitFloor3:
            self.labe211.setGeometry(rec6.x() + 10, rec6.y() + 10, rec6.width(), rec6.height())
        elif not self.hitSide3 and self.hitFloor3:
            self.labe211.setGeometry(rec6.x() - 10, rec6.y() - 10, rec6.width(), rec6.height())
        elif not self.hitFloor3 and not self.hitSide3:
            self.labe211.setGeometry(rec6.x() - 10, rec6.y() + 10, rec6.width(), rec6.height())
        elif self.hitSide3 and self.hitFloor3:
            self.labe211.setGeometry(rec6.x() + 10, rec6.y() - 10, rec6.width(), rec6.height())

    def moveBall2(self):
        rec7 = self.loptaKlasa.labelBall.geometry()
        if (rec7.y() >= 900):
            self.hitFloor4 = True
        elif (rec7.y() <= 0):
            self.hitFloor4 = False
        if (rec7.x() >= 1880):
            self.hitSide4 = True
        elif (rec7.x() <= 0):
            self.hitSide4 = False

        if self.hitSide4 and not self.hitFloor4:
            self.label5.setGeometry(rec7.x() - 10, rec7.y() + 10, rec7.width(), rec7.height())
        elif not self.hitSide4 and self.hitFloor4:
            self.label5.setGeometry(rec7.x() + 10, rec7.y() - 10, rec7.width(), rec7.height())
        elif not self.hitFloor4 and not self.hitSide4:
            self.label5.setGeometry(rec7.x() + 10, rec7.y() + 10, rec7.width(), rec7.height())
        elif self.hitSide4 and self.hitFloor4:
            self.label5.setGeometry(rec7.x() - 10, rec7.y() - 10, rec7.width(), rec7.height())

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
            self.arrowMovement2.ballY.append(broj2 - self.arr2h)
            self.label4.setGeometry(broj1 + 15, broj2 - self.arr2h, rec3.width(), rec3.height())
            if  not self.label5.isHidden():
             self.hitBall = HitBall()
             self.hitBall.hitBallSignal.connect(self.checkHit2)
             self.hitBall.start()

            else:

                    self.hitBall2 = HitBall()
                    self.hitBall2.hitBallSignal.connect(self.checkHit22)
                    self.hitBall2.start()

                    self.hitBall22 = HitBall()
                    self.hitBall22.hitBallSignal.connect(self.checkHit222)
                    self.hitBall22.start()


        else:
            self.hideArrow2()
            self.arrowMovement2.ballX = None

    def closeEvent(self, event):
        self.key_notifier.die()

    def hideArrow2(self):
        self.label4.hide()
        self.arr2h = 10
        self.arr2hidden = True
        self.arrowMovement2.is_done = True
        self.arrowMovement2.die()

    def hideArrow1(self):
        self.label3.hide()
        self.arr1h = 10
        self.arr1hidden = True
        self.arrowMovement.is_done = True
        self.arrowMovement.die()

    def checkHit(self):
        ballPosition = self.label5.geometry()

        if ballPosition.x() == self.arrowMovement.ballX:
            self.label5.hide()
            self.ballMovement.is_done = True
            self.ballMovement.die()


    def checkHit2(self):
        ballPosition = self.label5.geometry()

        if ballPosition.x() == self.arrowMovement2.ballX or ballPosition.x() + 1 == self.arrowMovement2.ballX or ballPosition.x() + 2 == self.arrowMovement2.ballX or ballPosition.x() + 3 == self.arrowMovement2.ballX or ballPosition.x() + 4 == self.arrowMovement2.ballX or ballPosition.x() +5  == self.arrowMovement2.ballX or ballPosition.x() + 6 == self.arrowMovement2.ballX or ballPosition.x() + 7 == self.arrowMovement2.ballX or ballPosition.x() + 8 == self.arrowMovement2.ballX:
            if ballPosition.y() in self.arrowMovement2.ballY or ballPosition.y() + 1 in self.arrowMovement2.ballY or ballPosition.y() + 2 in self.arrowMovement2.ballY or ballPosition.y() + 3 in self.arrowMovement2.ballY or ballPosition.y() + 4 in self.arrowMovement2.ballY or ballPosition.y() + 5 in self.arrowMovement2.ballY or ballPosition.y() + 6 in self.arrowMovement2.ballY or ballPosition.y() + 7 in self.arrowMovement2.ballY or ballPosition.y() + 8 in self.arrowMovement2.ballY:
               # self.arrowMovement2.ballY = []
                self.label5.hide()
                self.label5.destroy()
                if self.da == False:
                   self.labe21.setGeometry(ballPosition.x() + 10, ballPosition.y(), 100, 100)
                   self.labe211.setGeometry(ballPosition.x() - 100, ballPosition.y(), 100, 100)
                   self.hitFloor3 = False
                   self.hitSide3 = False
                   self.hitFloor2 = False
                   self.hitSide2 = False
                   self.da=True
                if self.bol ==False:

                 self.labe21.show()

                if self.bol2 == False:

                 self.labe211.show()




                self.label4.hide()


                self.arr2hidden = True
                self.arr2h = 10
                self.arrowMovement2.is_done = True
                self.arrowMovement2.die()



    def checkHit22(self):
        ballPosition = self.labe21.geometry()

        if ballPosition.x() == self.arrowMovement2.ballX or ballPosition.x() + 1 == self.arrowMovement2.ballX or ballPosition.x() + 2 == self.arrowMovement2.ballX or ballPosition.x() + 3 == self.arrowMovement2.ballX or ballPosition.x() + 4 == self.arrowMovement2.ballX or ballPosition.x() + 5 == self.arrowMovement2.ballX or ballPosition.x() + 6 == self.arrowMovement2.ballX or ballPosition.x() + 7 == self.arrowMovement2.ballX or ballPosition.x() + 8 == self.arrowMovement2.ballX:
            if ballPosition.y() in self.arrowMovement2.ballY or ballPosition.y() + 1 in self.arrowMovement2.ballY or ballPosition.y() + 2 in self.arrowMovement2.ballY or ballPosition.y() + 3 in self.arrowMovement2.ballY or ballPosition.y() + 4 in self.arrowMovement2.ballY or ballPosition.y() + 5 in self.arrowMovement2.ballY or ballPosition.y() + 6 in self.arrowMovement2.ballY or ballPosition.y() + 7 in self.arrowMovement2.ballY or ballPosition.y() + 8 in self.arrowMovement2.ballY:
                # self.arrowMovement2.ballY = []
                self.labe21.hide()
                self.labe21.destroy()
                self.bol =True


                self.label4.hide()


                self.arr2hidden = True
                self.arr2h = 10
                self.arrowMovement2.is_done = True
                self.arrowMovement2.die()

    def checkHit222(self):
        ballPosition = self.labe211.geometry()

        if ballPosition.x() == self.arrowMovement2.ballX or ballPosition.x() + 1 == self.arrowMovement2.ballX or ballPosition.x() + 2 == self.arrowMovement2.ballX or ballPosition.x() + 3 == self.arrowMovement2.ballX or ballPosition.x() + 4 == self.arrowMovement2.ballX or ballPosition.x() + 5 == self.arrowMovement2.ballX or ballPosition.x() + 6 == self.arrowMovement2.ballX or ballPosition.x() + 7 == self.arrowMovement2.ballX or ballPosition.x() + 8 == self.arrowMovement2.ballX:
            if ballPosition.y() in self.arrowMovement2.ballY or ballPosition.y() + 1 in self.arrowMovement2.ballY or ballPosition.y() + 2 in self.arrowMovement2.ballY or ballPosition.y() + 3 in self.arrowMovement2.ballY or ballPosition.y() + 4 in self.arrowMovement2.ballY or ballPosition.y() + 5 in self.arrowMovement2.ballY or ballPosition.y() + 6 in self.arrowMovement2.ballY or ballPosition.y() + 7 in self.arrowMovement2.ballY or ballPosition.y() + 8 in self.arrowMovement2.ballY:
                # self.arrowMovement2.ballY = []
                self.labe211.hide()
                self.labe211.destroy()
                self.bol2 = True

                self.label4.hide()


                self.arr2hidden = True
                self.arr2h = 10
                self.arrowMovement2.is_done = True
                self.arrowMovement2.die()

    def postaviLoptu(self, b):
        self.setCentralWidget(b)
        #self.v.addWidget(b)
        self.AddBall.is_done = True
        self.AddBall.die()
        #self.b.move(500, 100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimMoveDemo()
    sys.exit(app.exec_())
