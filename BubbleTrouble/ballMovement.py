from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot

import time


class BallMovement(QObject):

    ballMovementSignal = pyqtSignal()

    def __init__(self, brzina):
        super().__init__()

        self.is_done = False
        self.speed = brzina
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


    @pyqtSlot()
    def __work__(self):
        """
        A slot with no params.
        """
        while not self.is_done:
            self.ballMovementSignal.emit()
            if(self.speed < 0.01):
                time.sleep(0.02)
            else:
                time.sleep(self.speed)
