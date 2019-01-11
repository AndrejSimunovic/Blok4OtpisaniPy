import sys
import random

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow, QVBoxLayout, QProgressBar
<<<<<<< HEAD
import os
=======

>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8
from key_notifier import KeyNotifier
from ballMovement import BallMovement
from hitBall import HitBall
from arrowMovement import ArrowMovement
from ball import Ball
from addBall import AddBall

bolian = False


class SimMoveDemo(QMainWindow):

    def __init__(self, zivot1, zivot2, poeni1, poeni2, slika, level, pic_no):
        super().__init__()

        pix11 = QPixmap('player.png')
        pix22 = QPixmap('player2.png')
        # pix33 = QPixmap('arrow.png')
        # pix44 = QPixmap('arrow.png')
        pix55 = QPixmap('ball.png')
        pix66 = QPixmap('bal2.png')
        pix77 = QPixmap('present.png')

<<<<<<< HEAD
        self.labelStrelica1 = QLabel(self)
        self.labelStrelica2 = QLabel(self)
        self.labelPlayer1 = QLabel(self)
        self.labelPlayer2 = QLabel(self)
        self.labelVelikaLopta = QLabel(self)
        self.labelPozadina = QLabel(self)
        self.labelMalaLopticaDesna = QLabel(self)
        self.labelMalaLopticaLeva = QLabel(self)
=======
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label5 = QLabel(self)
        self.label6 = QLabel(self)
        self.labe21 = QLabel(self)
        self.labe211 = QLabel(self)
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8
        self.labelispis = QLabel(self)
        self.labelispis2 = QLabel(self)

        self.labellevel = QLabel(self)
        self.labelLives1 = QLabel(self)
        self.labelLives2 = QLabel(self)
        self.labelforce = QLabel(self)

        self.pbar = QProgressBar(self)

        self.timerP1 = QTimer(self)
        self.timerP2 = QTimer(self)

        self.timerSleep = QTimer(self)
        self.timerSleep2 = QTimer(self)

<<<<<<< HEAD
        self.timerStrelica1 = QTimer(self)
        self.timerStrelica2 = QTimer(self)

        oImage = QImage(slika)
=======
        oImage = QImage("fantasy_border.jpg")
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8

        self.hitFloorVelikaLopta = False
        self.hitSideVelikaLopta = False

        self.hitFloorMalaLopta1 = False
        self.hitSideMalaLoptaDesna = False
        self.VelikaLoptaPogodjena = False
        self.hitFloorMalaLopta2 = False
        self.hitSideMalaLopta2 = False

        self.LevaLopticaPostoji = False
        self.DesnaLopticaPostoji = False

        self.arr1h = 10
        self.arr2h = 10
        self.p1_speed = 15
        self.p2_speed = 15

        self.arr1hidden = True
        self.arr2hidden = True

        self.pix1 = pix11.scaledToHeight(84)
        self.pix1 = pix11.scaledToWidth(34)

        self.pix2 = pix22.scaledToHeight(84)
        self.pix2 = pix22.scaledToWidth(34)

        self.pix5 = pix55.scaledToHeight(384)
        self.pix5 = pix55.scaledToWidth(54)
        self.pix6 = pix66.scaledToHeight(384)

        self.pix6 = pix66.scaledToWidth(54)

        self.pix7 = pix77.scaledToWidth(34)
        self.pix7 = pix77.scaledToHeight(34)

        # self.pix3 = pix33.scaledToHeight(200)
        # self.pix3 = pix33.scaledToWidth(5)
        # self.pix4 = pix44.scaledToHeight(200)
        # self.pix4 = pix44.scaledToWidth(5)

        palette = QPalette()
        sImage = oImage.scaled(QSize(1920, 1080))
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.setWindowState(Qt.WindowFullScreen)
        self.__init_ui__(zivot1, zivot2, poeni1, poeni2, slika, level, pic_no)

        self.DesnaLopticaPogodjena = False
        self.LevaLopticaPogodjena = False
        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

        self.ballMovement = BallMovement()
        self.ballMovement.ballMovementSignal.connect(self.moveBallVelika)
        self.ballMovement.start()

        self.ballMovement3 = BallMovement()
        self.ballMovement3.ballMovementSignal.connect(self.moveBallMalaLopticaDesna)
        self.ballMovement3.start()

        self.ballMovement4 = BallMovement()
        self.ballMovement4.ballMovementSignal.connect(self.moveBallMalaLopticaLeva)
        self.ballMovement4.start()
        # self.v = QVBoxLayout()
<<<<<<< HEAD


    def __init_ui__(self, zivot1, zivot2, poeni1, poeni2, slika, level, pic_no):
=======
        self.loptaKlasa = Ball('ball.png', 2, 30, 30)
        self.AddBall = AddBall()
        self.AddBall.add_ball(self.loptaKlasa)
        self.AddBall.ball_signal.connect(self.postaviLoptu)
        self.ballMovement2 = BallMovement()
        self.ballMovement2.ballMovementSignal.connect(self.loptaKlasa.moveBall)

    def __init_ui__(self):
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8
        self.setWindowIcon(QtGui.QIcon('download.png'))
        self.setWindowTitle('BubbleTrouble')
        font = QtGui.QFont()
        font.setPointSize(40)
        self.slika = slika
        self.level = level
        self.pic_no = pic_no
        self.zivot1 = zivot1
        self.zivot2 = zivot2

        self.timerP1.start(20000)
        self.timerP1.timeout.connect(self.timer_func)
<<<<<<< HEAD
=======

        """"    OVO je za sad jedini nacin da se lopta pojavila 
        self.lopta = QLabel(self)
        Lopta = Ball('ball.png', 2, 100, 100)
        Lopta.setSize(80, 80)
        #self.lopta.showBall()
        self.lopta = Lopta.labelBall
        self.setCentralWidget(Lopta.labelBall)

        KORDINATE KRETANJA LOPTE TREBA POPRAVITI
        """
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8

        self.labelispis.setFont(font)
        self.labelispis.resize(100000, 100)
        self.labelispis.setGeometry(1500, 940, 400, 200)

        self.labelispis2.setFont(font)
        self.labelispis2.resize(100000, 100)
        self.labelispis2.setGeometry(0, 940, 400, 200)

        self.labelLives1.setFont(font)
        self.labelLives1.resize(100000, 100)
        self.labelLives1.setGeometry(10, 880, 400, 200)

        self.labelLives2.setFont(font)
        self.labelLives2.resize(1000, 100)
        self.labelLives2.setGeometry(1550, 880, 400, 200)

        self.pbar.setGeometry(500, 960, 1000, 40)
<<<<<<< HEAD
=======

        self.labellevel.setFont(font)
        self.labellevel.resize(100000, 100)
        self.labellevel.setGeometry(870, 940, 400, 200)

        self.label1.setPixmap(self.pix1)
        self.label1.setGeometry(1000, 900, 50, 50)
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8

        self.labellevel.setFont(font)
        self.labellevel.resize(100000, 100)
        self.labellevel.setGeometry(870, 940, 400, 200)

        self.labelPlayer1.setPixmap(self.pix1)
        self.labelPlayer1.setGeometry(1000, 900, 50, 50)

<<<<<<< HEAD
        self.labelPlayer2.setPixmap(self.pix2)
        self.labelPlayer2.setGeometry(900, 900, 50, 50)

        self.labelVelikaLopta.setPixmap(self.pix5)
        self.labelVelikaLopta.setGeometry(50, 50, 50, 50)

=======
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8
        self.labelforce.setPixmap(self.pix7)
        self.labelforce.setGeometry(-100, 0, 0, 0)
        self.labelforce.hide()

<<<<<<< HEAD

        self.labelMalaLopticaDesna.setPixmap(self.pix6)
        self.labelMalaLopticaDesna.setGeometry(50, 50, 50, 50)
        self.labelMalaLopticaDesna.hide()
        self.labelMalaLopticaLeva.setPixmap(self.pix6)
        self.labelMalaLopticaLeva.setGeometry(50, 50, 50, 50)
        self.labelMalaLopticaLeva.hide()
        self.labelStrelica1.resize(8, 950)
=======
        print("napravljena labela ubacena slika")

        self.labe21.setPixmap(self.pix6)
        self.labe21.setGeometry(50, 50, 50, 50)
        self.labe21.hide()
        self.labe211.setPixmap(self.pix6)
        self.labe211.setGeometry(50, 50, 50, 50)
        self.labe211.hide()
        self.label3.resize(8, 950)
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8
        pixmap1 = QtGui.QPixmap('arrow.png')
        self.pixmap = pixmap1.scaled(8, 950)
        self.labelStrelica1.setPixmap(self.pixmap)
        self.labelStrelica1.hide()

        self.labelStrelica2.resize(8, 950)
        pixmap1 = QtGui.QPixmap('arrow.png')
        self.pixmap = pixmap1.scaled(8, 950)
        self.labelStrelica2.setPixmap(self.pixmap)
        self.labelStrelica2.hide()

        self.labelPozadina.resize(1920, 100)
        pixmap1 = QtGui.QPixmap('ScoreBackground.jpg')
        self.pixmapScore = pixmap1.scaled(1920, 150)
        self.labelPozadina.setPixmap(self.pixmapScore)
        self.labelPozadina.setGeometry(0, 950, 1920, 145)

        self.x = 'Player1:'
        self.y = 'Player2:'
<<<<<<< HEAD

        self.lives1 = 3
        self.lives2 = 2
        self.poeni1 = poeni1
        self.poeni2 = poeni2

        self.lev = 'Level:'

        self.step = 0
=======
        self.score1 = 999999
        self.score2 = 999999
        self.lives1 = 3
        self.lives2 = 2

        self.lev = 'Level:'
        self.level_no = 1

        self.step = 0

        self.statusBar().setFont(font)
        self.labelispis.setText(str(self.x) + str(self.score1))
        self.labelispis2.setText(str(self.y) + str(self.score2))
        self.labellevel.setText(str(self.lev) + str(self.level_no))
        self.labelLives1.setText("Lives:" + str(self.lives1))
        self.labelLives2.setText("Lives:" + str(self.lives2))
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8

        self.statusBar().setFont(font)
        self.labelispis.setText(str(self.x) + str(self.poeni1))
        self.labelispis2.setText(str(self.y) + str(self.poeni2))
        self.labellevel.setText(str(self.lev) + str(self.level))
        self.labelLives2.setText("Lives:" + str(self.lives1))
        self.labelLives1.setText("Lives:" + str(self.lives2))
        self.ex2 = None
        self.show()

    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())

    def __update_position__(self, key):
<<<<<<< HEAD
        rec1 = self.labelPlayer1.geometry()
        rec2 = self.labelPlayer2.geometry()
=======
        rec1 = self.label1.geometry()
        rec2 = self.label2.geometry()
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8
        # rec3 = self.label3.geometry()
        # rec4 = self.label4.geometry()

        if key == Qt.Key_Right:
            if rec1.x() < 1880:
<<<<<<< HEAD
                self.labelPlayer1.setGeometry(rec1.x() + self.p1_speed, rec1.y(), rec1.width(), rec1.height())
=======
                self.label1.setGeometry(rec1.x() + self.p1_speed, rec1.y(), rec1.width(), rec1.height())
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8
                self.checkForceHitFromLeft1()
        elif key == Qt.Key_Up:
            if self.arr1hidden:
                geometrija = self.labelPlayer1.geometry()
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
<<<<<<< HEAD
                self.labelPlayer1.setGeometry(rec1.x() - self.p1_speed, rec1.y(), rec1.width(), rec1.height())
                self.checkForceHitFromRight1()
        if key == Qt.Key_D:
            if rec2.x() < 1880:
                self.labelPlayer2.setGeometry(rec2.x() + self.p2_speed, rec2.y(), rec2.width(), rec2.height())
=======
                self.label1.setGeometry(rec1.x() - self.p1_speed, rec1.y(), rec1.width(), rec1.height())
                self.checkForceHitFromRight1()
        if key == Qt.Key_D:
            if rec2.x() < 1880:
                self.label2.setGeometry(rec2.x() + self.p2_speed, rec2.y(), rec2.width(), rec2.height())
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8
                self.checkForceHitFromLeft2()
        elif key == Qt.Key_W:
            if self.arr2hidden:
                geometrija = self.labelPlayer2.geometry()
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
<<<<<<< HEAD
                self.labelPlayer2.setGeometry(rec2.x() - self.p2_speed, rec2.y(), rec2.width(), rec2.height())
                self.checkForceHitFromRight2()
        elif key == Qt.Key_Escape:
            self.close()

    def moveBallVelika(self):
        rec5 = self.labelVelikaLopta.geometry()
        igrac1 = self.labelPlayer1.geometry()
        igrac2 = self.labelPlayer2.geometry()
=======
                self.label2.setGeometry(rec2.x() - self.p2_speed, rec2.y(), rec2.width(), rec2.height())
                self.checkForceHitFromRight2()
        elif key == Qt.Key_Escape:
            self.close()
        elif key == Qt.Key_K:
            self.progressing()

    def moveBall(self):
        rec5 = self.label5.geometry()
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8
        if (rec5.y() == 900):
            self.hitFloorVelikaLopta = True
        elif (rec5.y() == 0):
            self.hitFloorVelikaLopta = False
        if (rec5.x() == 1880):
            self.hitSideVelikaLopta = True
        elif (rec5.x() == 0):
            self.hitSideVelikaLopta = False

        for i in range(0, 60):
            if igrac1.x() + i == rec5.x():
                if rec5.y() > 860 and rec5.y() < 900:
                    # self.label1.hide()dd
                    self.zivot1 = self.zivot1 - 1

                    self.ballMovement.die()
                    self.ballMovement3.die()
                    self.ballMovement4.die()

                    self.key_notifier.die()

                    self.close()
                    self.pbar.setValue(0)

                    self.ex2 = SimMoveDemo(self.zivot1, self.zivot2, self.poeni1, self.poeni2, self.slika, self.level, self.pic_no)

            if igrac2.x() + i == rec5.x():
                if rec5.y() > 860 and rec5.y() < 900:
                    # self.label1.hide()dd
                    self.zivot2 = self.zivot2 - 1
                    self.ballMovement.die()
                    self.ballMovement3.die()
                    self.ballMovement4.die()

                    self.key_notifier.die()

                    self.close()
                    self.ex2 = SimMoveDemo(self.zivot1, self.zivot2, self.poeni1, self.poeni2, self.slika, self.level, self.pic_no)

        self.labelLives2.setText('Lives: ' + str(self.zivot1))
        self.labelLives1.setText('Lives: ' + str(self.zivot2))

        if self.hitSideVelikaLopta and not self.hitFloorVelikaLopta:
            self.labelVelikaLopta.setGeometry(rec5.x() - 10, rec5.y() + 10, rec5.width(), rec5.height())
        elif not self.hitSideVelikaLopta and self.hitFloorVelikaLopta:
            self.labelVelikaLopta.setGeometry(rec5.x() + 10, rec5.y() - 10, rec5.width(), rec5.height())
        elif not self.hitFloorVelikaLopta and not self.hitSideVelikaLopta:
            self.labelVelikaLopta.setGeometry(rec5.x() + 10, rec5.y() + 10, rec5.width(), rec5.height())
        elif self.hitSideVelikaLopta and self.hitFloorVelikaLopta:
            self.labelVelikaLopta.setGeometry(rec5.x() - 10, rec5.y() - 10, rec5.width(), rec5.height())

    def moveBallMalaLopticaDesna(self):
        rec9 = self.labelMalaLopticaDesna.geometry()
        igrac1 = self.labelPlayer1.geometry()
        igrac2 = self.labelPlayer2.geometry()

        if (rec9.y() > 900):
            self.hitFloorMalaLopta1 = True
        elif (rec9.y() == 0):
            self.hitFloorMalaLopta1 = False
        if (rec9.x() == 1880):
            self.hitSideMalaLoptaDesna = True
        elif (rec9.x() == 0):
            self.hitSideMalaLoptaDesna = False

        if self.DesnaLopticaPostoji:
            for i in range(0, 60):
                if igrac1.x() + i == rec9.x():
                    if rec9.y() > 860 and rec9.y() < 900:
                        # self.label1.hide()dd
                        self.zivot1 = self.zivot1 - 1
                        self.ballMovement.die()
                        self.ballMovement3.die()
                        self.ballMovement4.die()

                        self.key_notifier.die()
                        self.close()
                        self.pbar.setValue(0)
                        self.ex2 = SimMoveDemo(self.zivot1, self.zivot2, self.poeni1, self.poeni2, self.slika, self.level, self.pic_no)

                if igrac2.x() + i == rec9.x():
                    if rec9.y() > 860 and rec9.y() < 900:
                        # self.label1.hide()dd
                        self.zivot2 = self.zivot2 - 1

                        self.ballMovement.die()
                        self.ballMovement3.die()
                        self.ballMovement4.die()
                        self.key_notifier.die()
                        self.close()
                        self.pbar.setValue(0)
                        self.ex2 = SimMoveDemo(self.zivot1, self.zivot2, self.poeni1, self.poeni2, self.slika, self.level, self.pic_no)

        self.labelLives2.setText('Lives: ' + str(self.zivot1))
        self.labelLives1.setText('Lives: ' + str(self.zivot2))

        if self.hitSideMalaLoptaDesna and not self.hitFloorMalaLopta1:
            self.labelMalaLopticaDesna.setGeometry(rec9.x() - 10, rec9.y() + 10, rec9.width(), rec9.height())
        elif not self.hitSideMalaLoptaDesna and self.hitFloorMalaLopta1:
            self.labelMalaLopticaDesna.setGeometry(rec9.x() + 10, rec9.y() - 10, rec9.width(), rec9.height())
        elif not self.hitFloorMalaLopta1 and not self.hitSideMalaLoptaDesna:
            self.labelMalaLopticaDesna.setGeometry(rec9.x() + 10, rec9.y() + 10, rec9.width(), rec9.height())
        elif self.hitSideMalaLoptaDesna and self.hitFloorMalaLopta1:
            self.labelMalaLopticaDesna.setGeometry(rec9.x() - 10, rec9.y() - 10, rec9.width(), rec9.height())

    def moveBallMalaLopticaLeva(self):
        rec6 = self.labelMalaLopticaLeva.geometry()
        igrac1 = self.labelPlayer1.geometry()
        igrac2 = self.labelPlayer2.geometry()

        if (rec6.y() >= 900):
            self.hitFloorMalaLopta2 = True
        elif (rec6.y() <= 0):
            self.hitFloorMalaLopta2 = False
        if (rec6.x() >= 1880):
            self.hitSideMalaLopta2 = False
        elif (rec6.x() <= 0):
            self.hitSideMalaLopta2 = True


        if self.LevaLopticaPostoji:
            for i in range(0, 60):
                if igrac1.x() + i == rec6.x():
                    if rec6.y() > 860 and rec6.y() < 900:
                        # self.label1.hide()dd
                        self.zivot1 = self.zivot1 - 1

                        self.ballMovement.die()
                        self.ballMovement3.die()
                        self.ballMovement4.die()

                        self.key_notifier.die()
                        self.close()
                        self.pbar.setValue(0)
                        self.ex2 = SimMoveDemo(self.zivot1, self.zivot2, self.poeni1, self.poeni2, self.slika, self.level, self.pic_no)

                if igrac2.x() + i == rec6.x():
                    if rec6.y() > 860 and rec6.y() < 900:
                        # self.label1.hide()dd
                        self.zivot2 = self.zivot2 - 1

                        self.ballMovement.die()
                        self.ballMovement3.die()
                        self.ballMovement4.die()
                        self.key_notifier.die()

                        self.close()
                        self.pbar.setValue(0)
                        self.ex2 = SimMoveDemo(self.zivot1, self.zivot2, self.poeni1, self.poeni2, self.slika, self.level, self.pic_no)


        self.labelLives2.setText('Lives: ' + str(self.zivot1))
        self.labelLives1.setText('Lives: ' + str(self.zivot2))

        if self.hitSideMalaLopta2 and not self.hitFloorMalaLopta2:
            self.labelMalaLopticaLeva.setGeometry(rec6.x() + 10, rec6.y() + 10, rec6.width(), rec6.height())
        elif not self.hitSideMalaLopta2 and self.hitFloorMalaLopta2:
            self.labelMalaLopticaLeva.setGeometry(rec6.x() - 10, rec6.y() - 10, rec6.width(), rec6.height())
        elif not self.hitFloorMalaLopta2 and not self.hitSideMalaLopta2:
            self.labelMalaLopticaLeva.setGeometry(rec6.x() - 10, rec6.y() + 10, rec6.width(), rec6.height())
        elif self.hitSideMalaLopta2 and self.hitFloorMalaLopta2:
            self.labelMalaLopticaLeva.setGeometry(rec6.x() + 10, rec6.y() - 10, rec6.width(), rec6.height())

    def arrowMove(self, lista):
        self.arr1hidden = False
        rec3 = self.labelStrelica1.geometry()
        rec1 = self.labelPlayer1.geometry()
        self.labelStrelica1.show()
        self.timerStrelica1.start(50)
        self.timerStrelica1.timeout.connect(self.proveriVisinuStrelice1)

        broj1 = lista[0]
        broj2 = lista[1]
        if (self.arr1h != 900):
            self.arr1h += 10
            self.arrowMovement.ballY.append(890)
            self.arrowMovement.ballY.append(0)
            self.arrowMovement.ballY.append(broj2 - self.arr1h)
            self.labelStrelica1.setGeometry(broj1 + 15, broj2 - self.arr1h, rec3.width(), rec3.height())
            if not self.labelVelikaLopta.isHidden():
                self.hitBall1Player1 = HitBall()
                self.hitBall1Player1.hitBallSignal.connect(self.checkHitVelikaLoptaPlayer1)
                self.hitBall1Player1.start()
            else:
                self.hitBall2Player1 = HitBall()
                self.hitBall2Player1.hitBallSignal.connect(self.checkHitMalaLopticaDesnaP1)
                self.hitBall2Player1.start()

                self.hitBall3Player1 = HitBall()
                self.hitBall3Player1.hitBallSignal.connect(self.checkHitMalaLopticaLevaP1)
                self.hitBall3Player1.start()
        else:
            self.hideArrow1()
            self.arrowMovement.ballX = None
            self.arrowMovement.ballY = []

    def proveriVisinuStrelice1(self):
        strelica1 = self.labelStrelica1.geometry()
        if (strelica1.y() <= 890):
            # self.arr1h = 10
            self.labelStrelica1.hide()
            self.arr1hidden = True
            self.arr1h = 10
            self.arrowMovement.is_done = True
            self.arrowMovement.die()

    def arrowMove2(self, lista):
        self.arr2hidden = False
        rec9 = self.labelStrelica2.geometry()
        rec1 = self.labelPlayer2.geometry()
        self.labelStrelica2.show()
        self.timerStrelica1.start(50)
        self.timerStrelica1.timeout.connect(self.proveriVisinuStrelice2)

        broj1 = lista[0]
        broj2 = lista[1]
        if (self.arr2h != 900):
            self.arr2h += 10
            self.arrowMovement2.ballY.append(890)
            self.arrowMovement2.ballY.append(0)
            self.arrowMovement2.ballY.append(broj2 - self.arr2h)
<<<<<<< HEAD
            self.labelStrelica2.setGeometry(broj1 + 15, broj2 - self.arr2h, rec9.width(), rec9.height())
            if not self.labelVelikaLopta.isHidden():
                self.hitBall = HitBall()
                self.hitBall.hitBallSignal.connect(self.checkHitVelikaLoptaPlayer2)
                self.hitBall.start()
=======
            self.label4.setGeometry(broj1 + 15, broj2 - self.arr2h, rec3.width(), rec3.height())
            if not self.label5.isHidden():
                self.hitBall = HitBall()
                self.hitBall.hitBallSignal.connect(self.checkHit2)
                self.hitBall.start()

>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8
            else:
                self.hitBall2 = HitBall()
                self.hitBall2.hitBallSignal.connect(self.checkHitMalaLopticaDesna)
                self.hitBall2.start()

<<<<<<< HEAD
                self.hitBall22 = HitBall()
                self.hitBall22.hitBallSignal.connect(self.checkHitMalaLopticaLeva)
                self.hitBall22.start()
=======
                self.hitBall2 = HitBall()
                self.hitBall2.hitBallSignal.connect(self.checkHit22)
                self.hitBall2.start()

                self.hitBall22 = HitBall()
                self.hitBall22.hitBallSignal.connect(self.checkHit222)
                self.hitBall22.start()


>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8
        else:
            self.hideArrow2()
            self.arrowMovement2.ballX = None
            self.arrowMovement2.ballY = []

    def proveriVisinuStrelice2(self):
        strelica2 = self.labelStrelica2.geometry()
        if (strelica2.y() <= 890):
            # self.arr1h = 10
            self.labelStrelica2.hide()
            self.arr2hidden = True
            self.arr2h = 10
            self.arrowMovement2.is_done = True
            self.arrowMovement2.die()

    def closeEvent(self, event):
        self.key_notifier.die()

    def hideArrow2(self):
        self.labelStrelica2.hide()
        self.labelStrelica2.destroy()
        self.arr2h = 10
        self.arr2hidden = True
        self.arrowMovement2.is_done = True
        self.arrowMovement2.die()

    def hideArrow1(self):
        self.labelStrelica1.hide()
        self.labelStrelica1.destroy()
        self.arr1h = 10
        self.arr1hidden = True
        self.arrowMovement.is_done = True
        self.arrowMovement.die()

    def timer_func(self):
        x = random.randint(0, 1880)
        self.labelforce.setGeometry(x, 828, 400, 200)
        self.labelforce.show()
        self.timerP2.start(10000)
        self.timerP2.timeout.connect(self.hide_force)

    def hide_force(self):
        self.labelforce.hide()
        self.labelforce.destroy()

<<<<<<< HEAD

    def checkForceHitFromLeft1(self):
        player1_position = self.labelPlayer1.geometry()
=======
    def checkForceHitFromLeft1(self):
        player1_position = self.label1.geometry()
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8
        force = self.labelforce.geometry()
        ran = random.randint(0, 1)
        if player1_position.x() + 34 >= force.x() and player1_position.x() <= force.x():
            self.labelforce.setGeometry(-100, 0, 0, 0)
            self.labelforce.hide()
            self.labelforce.destroy()
            if ran == 1:
                self.p1_speed = 25
            else:
                self.p1_speed = 5
            self.timerSleep.start(10000)
            self.timerSleep.timeout.connect(self.p1_normal_speed)

    def checkForceHitFromRight1(self):
<<<<<<< HEAD
        player1_position = self.labelPlayer1.geometry()
=======
        player1_position = self.label1.geometry()
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8
        force = self.labelforce.geometry()
        ran = random.randint(0, 1)
        if player1_position.x() <= force.x() + 34 and player1_position.x() >= force.x():
            self.labelforce.setGeometry(-100, 0, 0, 0)
            self.labelforce.hide()
            self.labelforce.destroy()
            if ran == 1:
                self.p1_speed = 25
            else:
                self.p1_speed = 5
            self.timerSleep.start(10000)
            self.timerSleep.timeout.connect(self.p1_normal_speed)

    def checkForceHitFromLeft2(self):
<<<<<<< HEAD
        player2_position = self.labelPlayer2.geometry()
=======
        player2_position = self.label2.geometry()
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8
        force = self.labelforce.geometry()
        ran = random.randint(0, 1)
        if player2_position.x() + 34 >= force.x() and player2_position.x() <= force.x():
            self.labelforce.setGeometry(-100, 0, 0, 0)
            self.labelforce.hide()
            self.labelforce.destroy()
            if ran == 1:
                self.p2_speed = 25
            else:
                self.p2_speed = 5
            self.timerSleep2.start(10000)
            self.timerSleep2.timeout.connect(self.p2_normal_speed)

    def checkForceHitFromRight2(self):
<<<<<<< HEAD
        player2_position = self.labelPlayer2.geometry()
=======
        player2_position = self.label2.geometry()
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8
        force = self.labelforce.geometry()
        ran = random.randint(0, 1)

        if player2_position.x() <= force.x() + 34 and player2_position.x() >= force.x():
            self.labelforce.setGeometry(-100, 0, 0, 0)
            self.labelforce.hide()
            self.labelforce.destroy()
            if ran == 1:
                self.p2_speed = 25
            else:
                self.p2_speed = 5
            self.timerSleep2.start(10000)
            self.timerSleep2.timeout.connect(self.p2_normal_speed)

    def p1_normal_speed(self):
        self.p1_speed = 15

    def p2_normal_speed(self):
        self.p2_speed = 15

    def checkHit(self):
        ballPosition = self.labelVelikaLopta.geometry()

        if ballPosition.x() == self.arrowMovement.ballX:
            self.labelVelikaLopta.hide()
            self.ballMovement.is_done = True
            self.ballMovement.die()

<<<<<<< HEAD
    def checkHitVelikaLoptaPlayer2(self):
        ballPosition = self.labelVelikaLopta.geometry()
=======
    def checkHit2(self):
        ballPosition = self.label5.geometry()
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8

        if ballPosition.x() == self.arrowMovement2.ballX or ballPosition.x() + 1 == self.arrowMovement2.ballX or ballPosition.x() + 2 == self.arrowMovement2.ballX or ballPosition.x() + 3 == self.arrowMovement2.ballX or ballPosition.x() + 4 == self.arrowMovement2.ballX or ballPosition.x() + 5 == self.arrowMovement2.ballX or ballPosition.x() + 6 == self.arrowMovement2.ballX or ballPosition.x() + 7 == self.arrowMovement2.ballX or ballPosition.x() + 8 == self.arrowMovement2.ballX:
            if ballPosition.y() in self.arrowMovement2.ballY or ballPosition.y() + 1 in self.arrowMovement2.ballY or ballPosition.y() + 2 in self.arrowMovement2.ballY or ballPosition.y() + 3 in self.arrowMovement2.ballY or ballPosition.y() + 4 in self.arrowMovement2.ballY or ballPosition.y() + 5 in self.arrowMovement2.ballY or ballPosition.y() + 6 in self.arrowMovement2.ballY or ballPosition.y() + 7 in self.arrowMovement2.ballY or ballPosition.y() + 8 in self.arrowMovement2.ballY:
                # self.arrowMovement2.ballY = []
<<<<<<< HEAD


                if self.VelikaLoptaPogodjena == False:
                    self.labelMalaLopticaDesna.setGeometry(ballPosition.x() + 10, ballPosition.y(), 100, 100)
                    self.labelMalaLopticaLeva.setGeometry(ballPosition.x() - 100, ballPosition.y(), 100, 100)
                    self.hitFloorMalaLopta2 = False
                    self.hitSideMalaLopta2 = False
                    self.hitFloorMalaLopta1 = False
                    self.hitSideMalaLoptaDesna = False
                    self.VelikaLoptaPogodjena = True
                    self.labelVelikaLopta.hide()
                    self.labelVelikaLopta.setGeometry(-500,-500,0,0)
                    self.poeni2 += 20
                    self.progressing(20)
                    self.labelispis.setText(str(self.x) + str(self.poeni1))
                    self.labelispis2.setText(str(self.y) + str(self.poeni2))

                if self.DesnaLopticaPogodjena == False:
                    self.labelMalaLopticaDesna.show()
                    self.DesnaLopticaPostoji = True

                if self.LevaLopticaPogodjena == False:
                    self.labelMalaLopticaLeva.show()
                    self.LevaLopticaPostoji = True

                self.labelStrelica2.hide()
=======
                self.label5.hide()
                self.label5.destroy()
                if self.da == False:
                    self.labe21.setGeometry(ballPosition.x() + 10, ballPosition.y(), 100, 100)
                    self.labe211.setGeometry(ballPosition.x() - 100, ballPosition.y(), 100, 100)
                    self.hitFloor3 = False
                    self.hitSide3 = False
                    self.hitFloor2 = False
                    self.hitSide2 = False
                    self.da = True
                if self.bol == False:
                    self.labe21.show()

                if self.bol2 == False:
                    self.labe211.show()

                self.label4.hide()

>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8
                self.arr2hidden = True
                self.arr2h = 10
                self.arrowMovement2.is_done = True
                self.arrowMovement2.die()

<<<<<<< HEAD
                self.ballMovement.is_done = True
                self.ballMovement.die()

    def checkHitMalaLopticaDesna(self):
        ballPosition = self.labelMalaLopticaDesna.geometry()
=======
    def checkHit22(self):
        ballPosition = self.labe21.geometry()
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8

        if ballPosition.x() == self.arrowMovement2.ballX or ballPosition.x() + 1 == self.arrowMovement2.ballX or ballPosition.x() + 2 == self.arrowMovement2.ballX or ballPosition.x() + 3 == self.arrowMovement2.ballX or ballPosition.x() + 4 == self.arrowMovement2.ballX or ballPosition.x() + 5 == self.arrowMovement2.ballX or ballPosition.x() + 6 == self.arrowMovement2.ballX or ballPosition.x() + 7 == self.arrowMovement2.ballX or ballPosition.x() + 8 == self.arrowMovement2.ballX:
            if ballPosition.y() in self.arrowMovement2.ballY or ballPosition.y() + 1 in self.arrowMovement2.ballY or ballPosition.y() + 2 in self.arrowMovement2.ballY or ballPosition.y() + 3 in self.arrowMovement2.ballY or ballPosition.y() + 4 in self.arrowMovement2.ballY or ballPosition.y() + 5 in self.arrowMovement2.ballY or ballPosition.y() + 6 in self.arrowMovement2.ballY or ballPosition.y() + 7 in self.arrowMovement2.ballY or ballPosition.y() + 8 in self.arrowMovement2.ballY:
                # self.arrowMovement2.ballY = []
<<<<<<< HEAD
                self.labelMalaLopticaDesna.hide()
                self.labelMalaLopticaDesna.setGeometry(-500, -500, 0, 0)
                self.DesnaLopticaPogodjena = True
                self.labelStrelica2.hide()
=======
                self.labe21.hide()
                self.labe21.destroy()
                self.bol = True

                self.label4.hide()

>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8
                self.arr2hidden = True
                self.arr2h = 10
                self.arrowMovement2.is_done = True
                self.arrowMovement2.die()
                self.arrowMovement2.start = False
                self.DesnaLopticaPostoji = False
                self.ballMovement3.is_done = True
                self.ballMovement3.die()

                self.arrowMovement2.ballY = []
                self.poeni2 += 50
                self.progressing(40)
                self.labelispis.setText(str(self.x) + str(self.poeni1))
                self.labelispis2.setText(str(self.y) + str(self.poeni2))



<<<<<<< HEAD
    def checkHitMalaLopticaLeva(self):
        ballPosition = self.labelMalaLopticaLeva.geometry()

        if ballPosition.x() == self.arrowMovement2.ballX or ballPosition.x() + 1 == self.arrowMovement2.ballX or ballPosition.x() + 2 == self.arrowMovement2.ballX or ballPosition.x() + 3 == self.arrowMovement2.ballX or ballPosition.x() + 4 == self.arrowMovement2.ballX or ballPosition.x() + 5 == self.arrowMovement2.ballX or ballPosition.x() + 6 == self.arrowMovement2.ballX or ballPosition.x() + 7 == self.arrowMovement2.ballX or ballPosition.x() + 8 == self.arrowMovement2.ballX:
            if ballPosition.y() in self.arrowMovement2.ballY or ballPosition.y() + 1 in self.arrowMovement2.ballY or ballPosition.y() + 2 in self.arrowMovement2.ballY or ballPosition.y() + 3 in self.arrowMovement2.ballY or ballPosition.y() + 4 in self.arrowMovement2.ballY or ballPosition.y() + 5 in self.arrowMovement2.ballY or ballPosition.y() + 6 in self.arrowMovement2.ballY or ballPosition.y() + 7 in self.arrowMovement2.ballY or ballPosition.y() + 8 in self.arrowMovement2.ballY:
                # self.arrowMovement2.ballY = []
                self.labelMalaLopticaLeva.hide()
                self.labelMalaLopticaLeva.setGeometry(-500, -500, 0, 0)
                self.LevaLopticaPogodjena = True
                self.labelStrelica2.hide()
=======
>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8
                self.arr2hidden = True
                self.arr2h = 10
                self.arrowMovement2.is_done = True
                self.arrowMovement2.die()
                self.arrowMovement2.start = False

                self.LevaLopticaPostoji = False
                self.ballMovement4.is_done = True
                self.ballMovement4.die()
                self.arrowMovement2.ballY = []
                self.poeni2 += 50
                self.progressing(40)
                self.labelispis.setText(str(self.x) + str(self.poeni1))
                self.labelispis2.setText(str(self.y) + str(self.poeni2))

    def progressing(self,poeni):
        self.step += poeni
        self.pbar.setValue(self.step)
        if self.step == 100:
            self.level += 1
            if self.pic_no < 5:
                self.pic_no += 1
            elif self.pic_no == 5:
                self.pic_no = 1
            self.step = 0
            self.pbar.setValue(self.step)
            self.labellevel.setText(str(self.lev) + str(self.level))
            self.slika = "fantasy_border_" + str(self.pic_no) + ".jpg"


            self.close()
            self.ex2 = SimMoveDemo(self.zivot1, self.zivot2, self.poeni1, self.poeni2, self.slika, self.level, self.pic_no)

            #oImage = QImage("fantasy_border_" + str(self.pic_no) + ".jpg")
            #palette = QPalette()
            #sImage = oImage.scaled(QSize(1920, 1080))
            #palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
            #self.setPalette(palette)

    def checkHitVelikaLoptaPlayer1(self):
        ballPosition = self.labelVelikaLopta.geometry()

        if ballPosition.x() == self.arrowMovement.ballX or ballPosition.x() + 1 == self.arrowMovement.ballX or ballPosition.x() + 2 == self.arrowMovement.ballX or ballPosition.x() + 3 == self.arrowMovement.ballX or ballPosition.x() + 4 == self.arrowMovement.ballX or ballPosition.x() + 5 == self.arrowMovement.ballX or ballPosition.x() + 6 == self.arrowMovement.ballX or ballPosition.x() + 7 == self.arrowMovement.ballX or ballPosition.x() + 8 == self.arrowMovement.ballX:
            if ballPosition.y() in self.arrowMovement.ballY or ballPosition.y() + 1 in self.arrowMovement.ballY or ballPosition.y() + 2 in self.arrowMovement.ballY or ballPosition.y() + 3 in self.arrowMovement.ballY or ballPosition.y() + 4 in self.arrowMovement.ballY or ballPosition.y() + 5 in self.arrowMovement.ballY or ballPosition.y() + 6 in self.arrowMovement.ballY or ballPosition.y() + 7 in self.arrowMovement.ballY or ballPosition.y() + 8 in self.arrowMovement.ballY:
                # self.arrowMovement2.ballY = []


<<<<<<< HEAD
                if self.VelikaLoptaPogodjena == False:
                    self.labelMalaLopticaDesna.setGeometry(ballPosition.x() + 10, ballPosition.y(), 100, 100)
                    self.labelMalaLopticaLeva.setGeometry(ballPosition.x() - 100, ballPosition.y(), 100, 100)
                    self.hitFloorMalaLopta2 = False
                    self.hitSideMalaLopta2 = False
                    self.hitFloorMalaLopta1 = False
                    self.hitSideMalaLoptaDesna = False
                    self.VelikaLoptaPogodjena = True
                    self.labelVelikaLopta.hide()
                    self.labelVelikaLopta.setGeometry(-500, -500, 0, 0)
                    self.poeni1 += 20
                    self.progressing(20)
                    self.labelispis.setText(str(self.x) + str(self.poeni1))
                    self.labelispis2.setText(str(self.y) + str(self.poeni2))

                if self.DesnaLopticaPogodjena == False:
                    self.labelMalaLopticaDesna.show()
                    self.DesnaLopticaPostoji = True

                if self.LevaLopticaPogodjena == False:
                    self.labelMalaLopticaLeva.show()
                    self.LevaLopticaPostoji = True

                self.labelStrelica1.hide()
                self.arr1hidden = True
                self.arr1h = 10
                self.arrowMovement.is_done = True
                self.arrowMovement.die()

                self.ballMovement.is_done = True
                self.ballMovement.die()

    def checkHitMalaLopticaDesnaP1(self):
        ballPosition = self.labelMalaLopticaDesna.geometry()

        if ballPosition.x() == self.arrowMovement.ballX or ballPosition.x() + 1 == self.arrowMovement.ballX or ballPosition.x() + 2 == self.arrowMovement.ballX or ballPosition.x() + 3 == self.arrowMovement.ballX or ballPosition.x() + 4 == self.arrowMovement.ballX or ballPosition.x() + 5 == self.arrowMovement.ballX or ballPosition.x() + 6 == self.arrowMovement.ballX or ballPosition.x() + 7 == self.arrowMovement.ballX or ballPosition.x() + 8 == self.arrowMovement.ballX:
            if ballPosition.y() in self.arrowMovement.ballY or ballPosition.y() + 1 in self.arrowMovement.ballY or ballPosition.y() + 2 in self.arrowMovement.ballY or ballPosition.y() + 3 in self.arrowMovement.ballY or ballPosition.y() + 4 in self.arrowMovement.ballY or ballPosition.y() + 5 in self.arrowMovement.ballY or ballPosition.y() + 6 in self.arrowMovement.ballY or ballPosition.y() + 7 in self.arrowMovement.ballY or ballPosition.y() + 8 in self.arrowMovement.ballY:
                # self.arrowMovement2.ballY = []
                self.labelMalaLopticaDesna.hide()
                self.labelMalaLopticaDesna.setGeometry(-500, -500, 0, 0)
                self.DesnaLopticaPogodjena = True
                self.labelStrelica1.hide()
                self.arr1hidden = True
                self.arr1h = 10
                self.arrowMovement.is_done = True
                self.arrowMovement.die()
                self.arrowMovement.start = False

                self.DesnaLopticaPostoji = False
                self.ballMovement3.is_done = True
                self.ballMovement3.die()
                self.arrowMovement.ballY = []
                self.poeni1 += 50
                self.progressing(40)
                self.labelispis.setText(str(self.x) + str(self.poeni1))
                self.labelispis2.setText(str(self.y) + str(self.poeni2))



    def checkHitMalaLopticaLevaP1(self):
        ballPosition = self.labelMalaLopticaLeva.geometry()

        if ballPosition.x() == self.arrowMovement.ballX or ballPosition.x() + 1 == self.arrowMovement.ballX or ballPosition.x() + 2 == self.arrowMovement.ballX or ballPosition.x() + 3 == self.arrowMovement.ballX or ballPosition.x() + 4 == self.arrowMovement.ballX or ballPosition.x() + 5 == self.arrowMovement.ballX or ballPosition.x() + 6 == self.arrowMovement.ballX or ballPosition.x() + 7 == self.arrowMovement.ballX or ballPosition.x() + 8 == self.arrowMovement.ballX:
            if ballPosition.y() in self.arrowMovement.ballY or ballPosition.y() + 1 in self.arrowMovement.ballY or ballPosition.y() + 2 in self.arrowMovement.ballY or ballPosition.y() + 3 in self.arrowMovement.ballY or ballPosition.y() + 4 in self.arrowMovement.ballY or ballPosition.y() + 5 in self.arrowMovement.ballY or ballPosition.y() + 6 in self.arrowMovement.ballY or ballPosition.y() + 7 in self.arrowMovement.ballY or ballPosition.y() + 8 in self.arrowMovement.ballY:
                # self.arrowMovement2.ballY = []
                self.labelMalaLopticaLeva.hide()
                self.labelMalaLopticaLeva.setGeometry(-500, -500, 0, 0)
                self.LevaLopticaPogodjena = True
                self.labelStrelica1.hide()
                self.arr1hidden = True
                self.arr1h = 10
                self.arrowMovement.is_done = True
                self.arrowMovement.die()


                self.LevaLopticaPostoji = False
                self.ballMovement4.is_done = True
                self.ballMovement4.die()
                self.arrowMovement.ballY = []
                self.poeni1 += 50
                self.progressing(40)
                self.labelispis.setText(str(self.x) + str(self.poeni1))
                self.labelispis2.setText(str(self.y) + str(self.poeni2))
=======
    def postaviLoptu(self, b):
        self.setCentralWidget(b)
        # self.v.addWidget(b)
        self.AddBall.is_done = True
        self.AddBall.die()
        # self.b.move(500, 100)

    def progressing(self):
        self.step += 1
        self.pbar.setValue(self.step)
        if self.step == 100:
            self.level_no += 1
            self.step = 0
            self.pbar.setValue(self.step)
            self.labellevel.setText(str(self.lev) + str(self.level_no))

>>>>>>> e39e4c1c8aa684a75c8199e78325c28f27deaad8

if __name__ == '__main__':
    app = QApplication(sys.argv)
    zivot1 = 3
    zivot2 = 3
    poeni1 = 0
    poeni2 = 0
    level = 1
    pic_no = 1
    slika = "fantasy_border_1.jpg"

    ex = SimMoveDemo(zivot1, zivot2, poeni1, poeni2, slika, level, pic_no)
    sys.exit(app.exec_())
