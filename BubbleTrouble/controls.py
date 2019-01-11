from PyQt5 import QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton


class Controls(QWidget):

    def __init__(self):
        super().__init__()

        oImage = QImage("cntrls.jpg")

        self.label = QLabel(self)

        self.left = 600
        self.top = 200
        self.width = 1080
        self.height = 600

        palette = QPalette()
        sImage = oImage.scaled(QSize(1080, 600))
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.__init_ui__()

    def __init_ui__(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon('download.png'))

        self.setWindowTitle("Controls")

        button = QPushButton('BACK', self)
        button.resize(143, 43)
        button.move(937, 0)
        button.clicked.connect(self.back_on_click)

        #self.show()

    def back_on_click(self):
        self.close()
