from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot

import time


class AddBall(QObject):

    ball_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        self.bals = []
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

    def add_ball(self, b):
        self.bals.append(b)

    def rem_ball(self, b):
        self.balls.remove(b)

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
            for b in self.bals:
                self.ball_signal.emit(b)
            time.sleep(0.05)
