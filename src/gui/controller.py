import psutil
import logging as log
from PyQt5.QtCore import QTimer, pyqtSignal, QObject

class Controller:
    """Main controller instance"""

    def __init__(self, model, view):
        print("Building controller")
        self.model = model
        self.view = view
        print("QTimer initialized")
        self.timer = QTimer()
        print("QTimer connected to update_frame")
        self.timer.timeout.connect(self.update_frame)  # Gives warn but breaks if removed. Works just fine
        print("QTimer started with 30 ms interval")
        self.timer.start(30)  # updates every 30 ms

        # Connect to view signals
        self.view.capture_signal.connect(self.capture_frame)

        # Connect to model signals
        self.model.text_update_signal.connect(self.update_text)
        self.model.button_update_signal.connect(self.update_button)
        self.model.solve_signal.connect(self.solve_done)

    def update_frame(self):
        """Updates UI camera view with new camera frame"""
        print("Getting frame in update")
        self.log_system_stats()
        frame = self.model.get_frame()
        frame1 = self.model.handle_captured() #Run it here because broken
        print("Got frame in update")
        if frame is not None:
            print("Frame is not none")
            self.view.view_update(frame)
            print("Updated frame")

    def capture_frame(self):
        """Captures a frame from the camera"""
        print("Getting frame in capture")
        frame = self.model.get_frame()
        print("Got frame in capture")
        self.model.handle_captured(frame)
        if frame is not None:
            pass

    def solve_done(self):
        # reroute button for next_solve
        self.view.button.clicked.disconnect(self.view.on_capture)
        self.view.button.clicked.connect(self.view.next_solve)

    def next_solve(self):
        """Gets next solve step"""
        next_entry = self.model.SolveData.get_next_entry()
        if next_entry is not None:
            pass
        else:
            # No more entries
            print("No more entries in solve data")
            self.update_text("Cube is solved")
            self.update_button("Capture")

            # reroute button back to on_capture
            self.view.button.clicked.disconnect(self.view.next_solve)
            self.view.button.clicked.connect(self.view.on_capture)

    def update_text(self, text):
        self.view.update_steps(text)

    def update_button(self, text):
        self.view.update_button(text)

    def stop(self):
        """Stops the app"""
        self.timer.stop()
        self.model.release()

    def log_system_stats(self):
        """Logs system statistics for troubleshooting"""
        cpu_usage = psutil.cpu_percent()
        memory_info = psutil.virtual_memory()
        log.info(f"CPU Usage: {cpu_usage}%")
        log.info(f"Memory Usage: {memory_info.percent}%")