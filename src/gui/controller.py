from PyQt5.QtCore import QTimer, pyqtSignal, QObject

class Controller:
    """Main controller instance"""
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame) #Gives warn but breaks if removed. Works just fine
        self.timer.start(30) #updates every 30 ms

        #Connect to view
        self.view.capture_signal.connect(self.capture_frame)

    def update_frame(self):
        """Updates UI camera view with new camera frame"""
        frame = self.model.get_frame()
        if frame is not None:
            self.view.view_update(frame)

    def capture_frame(self):
        """Captures a frame from the camera"""
        frame = self.model.get_frame()
        self.model.handle_captured(frame)
        if frame is not None:
            pass

    def next_solve(self):
        """Gets next solve step"""
        data = self.model.SolveData.get_data() #eh?

    def stop(self):
        """Stops the app"""
        self.timer.stop()
        self.model.release()