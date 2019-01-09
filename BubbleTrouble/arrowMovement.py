from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot

import time


class ArrowMovement(QObject):

    arrowMovementSignal = pyqtSignal(list)

    def __init__(self):
        super().__init__()

        self.lista = []
        self.ballX = None
        self.ballY = []
        self.is_done = False

        self.thread = QThread()
        # move the Worker object to the Thread object
        # "push" self from the current thread to this thread
        self.moveToThread(self.thread)
        # Connect Thread started signal to Worker operational slot method
        self.thread.started.connect(self.__work__)

    def start(self):
        """
        Start notifications.
        """
        self.thread.start()

    def die(self):
        """
        End notifications.
        """
        self.is_done = True
        self.thread.quit()

    def add_list(self, num):
        self.lista.append(num)

    def rem_list(self, num):
        self.lista.remove(num)

    #def add_ball_list(self, num):
     #   self.ballList.append(num)

    @pyqtSlot()
    def __work__(self):
        """
        A slot with no params.
        """
        while not self.is_done:
            self.arrowMovementSignal.emit(self.lista)
            time.sleep(0.03)
