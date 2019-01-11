import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QPushButton
from controls import Controls
from pocetni import SimMoveDemo
from single_player import SimMoveDemo1

class Menu(QMainWindow):

    def __init__(self):
        super().__init__()

        oImage = QImage("hqdefault.jpg")

        self.label = QLabel(self)

        self.left = 600
        self.top = 200
        self.width = 600
        self.height = 400

        palette = QPalette()
        sImage = oImage.scaled(QSize(600, 400))
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.__init_ui__()

    def __init_ui__(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon('download.png'))

        self.setWindowTitle("Menu")

        button1 = QPushButton('1 PLAYER', self)
        button1.resize(143, 43)
        button1.move(77, 186)
        button1.clicked.connect(self.one_players_on_click)

        button2 = QPushButton('2 PLAYERS', self)
        button2.resize(143, 43)
        button2.move(77, 229)
        button2.clicked.connect(self.two_players_on_click)

        button3 = QPushButton('CONTROLS', self)
        button3.resize(143, 44)
        button3.move(77, 272)

        button3.clicked.connect(self.controls_on_click)

        button4 = QPushButton('QUIT', self)
        button4.resize(143, 43)
        button4.move(77, 316)

        button4.clicked.connect(self.quit_on_click)
        self.show()

    def controls_on_click(self):
        self.controls_window = Controls()
        self.controls_window.show()

    def two_players_on_click(self):
        zivot1 = 3
        zivot2 = 3
        poeni1 = 0
        poeni2 = 0
        level = 1
        pic_no = 1
        slika = "fantasy_border_1.jpg"
        speed = 0.08
        self.two = SimMoveDemo(zivot1, zivot2, poeni1, poeni2, slika, level, pic_no, speed)
        self.two.show()
        self.close()

    def one_players_on_click(self):
        zivot1 = 3
        zivot2 = 3
        poeni1 = 0
        poeni2 = 0
        level = 1
        pic_no = 1
        slika = "fantasy_border_1.jpg"
        speed = 0.08
        self.one = SimMoveDemo1(zivot1, zivot2, poeni1, poeni2, slika, level, pic_no, speed)
        self.one.show()
        self.close()

    def quit_on_click(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())
