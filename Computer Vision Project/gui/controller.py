from PyQt5.QtCore import QTimer, pyqtSignal, QObject

class CameraSignals(QObject): #Observer pattern essentially
    capture_requested = pyqtSignal()

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame) #Gives warn but breaks if removed. Works just fine
        self.timer.start(30) #updates every 30 ms

        #Connect to view
        self.view.capture_signal.connect(self.capture_frame)

    def update_frame(self):
        frame = self.model.get_frame()
        if frame is not None:
            self.view.view_update(frame)

    def capture_frame(self): #Merge with above?
        frame = self.model.get_frame()
        if frame is not None:
            self.model.handle_captured(frame)

    def stop(self):
        self.timer.stop()
        self.model.release()