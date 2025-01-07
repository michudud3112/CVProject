import os
import cv2
import logging
import numpy as np
from cleaning.mask import ImageProcessor
from solving.solver import Solver
from PyQt5.QtCore import pyqtSignal, QObject, QTimer

class Camera(QObject):
    """Main class for handling camera and related"""
    text_update_signal = pyqtSignal(str)
    button_update_signal = pyqtSignal(str)
    solve_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.cap = cv2.VideoCapture(0) # Init the cam TODO: replace with kinect

        self.save_dir = os.path.join(os.path.dirname(__file__), "imgs")
        if not os.path.exists(self.save_dir): # for issues with perms
            try:
                os.makedirs(self.save_dir)
                logging.info(f"Created directory: {self.save_dir}")
            except PermissionError:
                logging.error(f"ERROR: No permission to create directory {self.save_dir}")
                raise
            except Exception as e:
                logging.error(f"ERROR creating directory: {str(e)}")
                raise

    def get_frame(self):
        """Gets a frame from camera instance"""
        ret, frame = self.cap.read() # Get a frame

        if ret:
            save_path = os.path.join(self.save_dir, "temp.jpg")

            try:
                if cv2.imwrite(save_path, frame):
                    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                else:
                    logging.info(f"Failed to save image to {save_path}")
            except PermissionError:
                logging.error(f"ERROR: No permissions to write to: {save_path}")
            except Exception as e:
                logging.error(f"ERROR saving image: {str(e)}")

        return None

    def release(self):
        """Stops video capture"""
        self.cap.release()

    def handle_captured(self, frame):
        """Handles a captured frame. Invokes face detection. If 6 are found, begins solving"""
        # Start with cleaning.
        logging.info("Cleaning")

        img_processor = ImageProcessor(os.path.join(self.save_dir, "temp.jpg"))

        clean, posit, size = img_processor.process() # function call
        if not clean:
            logging.warning("Cleaning failed")
            self.update_text("Taking image failed. Please try again.")
            return

        res = np.empty((3, 3), dtype=object)

        # Get depth from kinect and merge
        # Posit gets used for depth

        for i in range(3):
            for j in range(3):
                res[i, j] = (size[i][j], None)

        FaceData.add_data(size)
        self.update_text(f"Image {FaceData.get_size()} captured successfully")

        if FaceData.get_size() == 6:
            logging.info("Enough data")
            self.update_text("All images captured")

            QTimer.singleShot(1000, self.handle_solve) #Delay before solving

    def handle_solve(self):
        """Invokes cube solving with detected faces"""
        logging.info("Solving")
        self.update_text("Starting solving")
        self.update_button("Next solve")

        data = FaceData.get_data()

        solver = Solver(data)
        solved_data = solver.solve()
        logging.info(solved_data) # debug

        SolveData.add_data(solved_data)

        #Rerouting button for next_solve
        self.solve_signal.emit()


    def update_text(self, text):
        self.text_update_signal.emit(text)

    def update_button(self, text):
        self.button_update_signal.emit(text)


class SolveData:
    """Storage for solve data"""
    data = [] # 6 3x3 arrays of sizes, with corresponding depths
    idx = 0

    @classmethod
    def add_data(cls, new):
        cls.data.append(new)

    @classmethod
    def get_data(cls):
        return cls.data

    @classmethod
    def next_entry(cls):
        if cls.idx < len(cls.data):
            entry = cls.data[cls.current_index]
            cls.indx += 1
            return entry
        else:
            return None

    @classmethod
    def reset_idx(cls):
        cls.idx = 0

class FaceData:
    """Storage for detected face data"""
    data = []

    @classmethod
    def add_data(cls, new):
        cls.data.append(new)

    @classmethod
    def get_data(cls):
        return cls.data

    @classmethod
    def kill_data(cls):
        cls.data.clear()

    @classmethod
    def get_size(cls):
        return len(cls.data)