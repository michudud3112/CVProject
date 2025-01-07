from PyQt5.QtCore import QTimer, pyqtSignal, QObject
import logging as log

class Controller:
    """Main controller instance"""
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame) #Gives warn but breaks if removed. Works just fine
        self.timer.start(30) #updates every 30 ms

        #Connect to view signals
        self.view.capture_signal.connect(self.capture_frame)

        #Connect to model signals
        self.model.text_update_signal.connect(self.update_text)
        self.model.button_update_signal.connect(self.update_button)
        self.model.solve_signal.connect(self.solve_done)

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

    def solve_done(self):
        #reroute button for next_solve
        self.view.button.clicked.disconnect(self.view.on_capture)
        self.view.button.clicked.connect(self.view.next_solve)

    def next_solve(self):
        """Gets next solve step"""
        next_entry = self.model.SolveData.get_next_entry()
        if next_entry is not None:
            pass
        else:
            #No more entries
            log.info("No more entries in solve data")
            self.update_text("Cube is solved")
            self.update_button("Capture")

            #reroute button back to on_capture
            self.view.button.clicked.disconnect(self.view.next_solve)
            self.view.button.clicked.connect(self.view.on_capture)

    def update_text(self, text):
        self.view.update_steps(text)

    def update_button(self,text):
        self.view.update_button(text)

    def stop(self):
        """Stops the app"""
        self.timer.stop()
        self.model.release()