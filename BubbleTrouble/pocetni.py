import sys

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize,QTimer
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

from key_notifier import KeyNotifier


class SimMoveDemo(QWidget):


    def __init__(self):
        super().__init__()

        pix11 = QPixmap('player.png')
        pix22 = QPixmap('player2.png')
        #pix33 = QPixmap('arrow.png')
        #pix44 = QPixmap('arrow.png')

        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)

        self.timerP1 = QTimer(self)
        self.timerP1.setInterval(2000)
        self.timerP1.setSingleShot(True)

        self.timerP2 = QTimer(self)
        self.timerP2.setInterval(2000)
        self.timerP2.setSingleShot(True)

        oImage = QImage("fantasy_border.png")

        self.pix1 = pix11.scaledToHeight(84)
        self.pix1 = pix11.scaledToWidth(34)

        self.pix2 = pix22.scaledToHeight(204)
        self.pix2 = pix22.scaledToWidth(34)

        #self.pix3 = pix33.scaledToHeight(200)
        #self.pix3 = pix33.scaledToWidth(5)
        #self.pix4 = pix44.scaledToHeight(200)
        #self.pix4 = pix44.scaledToWidth(5)

        palette = QPalette()
        sImage = oImage.scaled(QSize(1920, 1080))
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.setWindowState(Qt.WindowFullScreen)
        self.__init_ui__()

        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

    def __init_ui__(self):

        self.label1.setPixmap(self.pix1)
        self.label1.setGeometry(1000, 900, 50, 50)

        self.label2.setPixmap(self.pix2)
        self.label2.setGeometry(900, 900, 50, 50)

        self.label3.resize(8, 900)
        pixmap1 = QtGui.QPixmap('arrow.png')
        self.pixmap = pixmap1.scaled(8, 900)
        self.label3.setPixmap(self.pixmap)
        self.label3.hide()

        self.label4.resize(8, 900)
        pixmap1 = QtGui.QPixmap('arrow.png')
        self.pixmap = pixmap1.scaled(8, 900)
        self.label4.setPixmap(self.pixmap)
        self.label4.hide()

        self.setWindowTitle('Sim Slide')

        self.show()

    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())


    def __update_position__(self, key):
        rec1 = self.label1.geometry()
        rec2 = self.label2.geometry()
        rec3 = self.label3.geometry()
        rec4 = self.label4.geometry()

        if key == Qt.Key_Right:
            if rec1.x() < 1880:
                self.label1.setGeometry(rec1.x() + 15, rec1.y(), rec1.width(), rec1.height())
        elif key == Qt.Key_Up:
            if not self.timerP1.isActive():
                self.label3.show()
                self.label3.setGeometry(rec1.x() + 15, rec1.y() - 900 , rec3.width(),rec3.height())
                self.timerP1.start()
                self.timerP1.timeout.connect(self.hideArrow1)
        elif key == Qt.Key_Left:
            if rec1.x() > 15:
                self.label1.setGeometry(rec1.x() - 15, rec1.y(), rec1.width(), rec1.height())

        if key == Qt.Key_D:
            if rec2.x() < 1880:
                self.label2.setGeometry(rec2.x() + 15, rec2.y(), rec2.width(), rec2.height())
        elif key == Qt.Key_W:
            if not self.timerP2.isActive():
                self.label4.show()
                self.label4.setGeometry(rec2.x() + 15, rec2.y() - 900 , rec4.width(),rec4.height())
                self.timerP2.start()
                self.timerP2.timeout.connect(self.hideArrow2)
        elif key == Qt.Key_A:
            if rec2.x() > 15:
                self.label2.setGeometry(rec2.x() - 15, rec2.y(), rec2.width(), rec2.height())

    def closeEvent(self, event):
        self.key_notifier.die()

    def hideArrow2(self):
        self.label4.hide()

    def hideArrow1(self):
        self.label3.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimMoveDemo()
    sys.exit(app.exec_())
