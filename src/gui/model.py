import json
import os
import cv2
import logging as log
import numpy as np
from cleaning.mask import ImageProcessor
from solving.solver import Solver
from PyQt5.QtCore import pyqtSignal, QObject, QTimer
from pyfreenect2 import Freenect2Device as Device, getDefaultDeviceSerialNumber
from pyfreenect2 import SyncMultiFrameListener as FrameListener, Frame

class Camera(QObject):
    """Main class for handling camera and related"""
    text_update_signal = pyqtSignal(str)
    button_update_signal = pyqtSignal(str)
    solve_signal = pyqtSignal()
    error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        try:
            self.kinect = Kinect()
            self.kinect.start()
        except Exception as e:
            log.error(f"Failed to start app: {str(e)}")
            self.error_signal.emit(f"Failed to start app: {str(e)}")

        self.captured_frame = None


        self.save_dir = os.path.join(os.path.dirname(__file__), "data")
        if not os.path.exists(self.save_dir):  # for issues with perms
            try:
                os.makedirs(self.save_dir)
                print(f"Created directory: {self.save_dir}")
            except PermissionError:
                log.error(f"ERROR: No permission to create directory {self.save_dir}")
                raise
            except Exception as e:
                log.error(f"ERROR creating directory: {str(e)}")
                raise

    def get_frame(self):
        """Gets a frame from camera instance"""
        print("  Capturing frame")
        self.captured_frame = self.kinect.get_kinect_frame()  # Get a frame
        print("  Capture frame")

        if self.captured_frame is not None:
            print("  Frame is not none")
            save_path = os.path.join(self.save_dir, "temp.jpg")



            try:
                color_frame = self.captured_frame.getFrame(Frame.COLOR)
                rgb_data = color_frame.getRGBData()
                print(f"  Color Frame Shape: {color_frame.getHeight()}x{color_frame.getWidth()}")

                height, width = rgb_data.shape[:2]
                crop_size = int(min(height, width) * 0.3)
                start_y = (height - crop_size) // 2
                start_x = (width - crop_size) // 2
                cropped_image = rgb_data[start_y:start_y + crop_size, start_x:start_x + crop_size]

                if cv2.imwrite(save_path, cropped_image):
                    print("  Wrote frame")

                    #del self.captured_frame

                    return cv2.cvtColor(rgb_data, cv2.COLOR_BGR2RGB)
                else:
                    print(f"Failed to save image to {save_path}")
            except PermissionError:
                log.error(f"ERROR: No permissions to write to: {save_path}")
            except Exception as e:
                log.error(f"ERROR: {str(e)}")

        print("  Frame is none")
        return None

    def release(self):
        """Stops video capture"""
        self.kinect.stop()

    def handle_captured(self):
        """Handles a captured frame. Invokes face detection. If 6 are found, begins solving"""
        # Start with cleaning.
        print("Cleaning")

        img_processor = ImageProcessor(os.path.join(self.save_dir, "temp.jpg"))

        clean, posit, size = img_processor.process()  # function call
        if not clean:
            log.warning("Cleaning failed")
            self.update_text("Taking image failed. Please try again.")
            return

        res = np.empty((3, 3), dtype=object)

        # Get depth from stored kinect frame and merge
        depth = self.captured_frame.getFrame(Frame.DEPTH)

        for i in range(3):
            for j in range(3):
                x, y = posit[i][j]
                h, w = size[i][j]
                depth = depth[i + h // 2, j + w //2]
                res[i, j] = (size[i][j], depth)

        FaceData.add_data(size)
        face_data_path = os.path.join(self.save_dir, "data.json")
        with open(face_data_path, 'w') as f:
            json.dump(FaceData.get_data(), f)
        print(f"Face data written to {face_data_path}")

        self.update_text(f"Image {FaceData.get_size()} captured successfully")

        if FaceData.get_size() == 6:
            print("Enough data")
            self.update_text("All images captured")

            QTimer.singleShot(1000, self.handle_solve)  # Delay before solving

    def handle_solve(self):
        """Invokes cube solving with detected faces"""
        print("Solving")
        self.update_text("Starting solving")
        self.update_button("Next solve")

        data = FaceData.get_data()

        solver = Solver(data)
        solved_data = solver.solve()
        print(solved_data)  # debug

        SolveData.add_data(solved_data)

        # Rerouting button for next_solve
        self.solve_signal.emit()

    def update_text(self, text):
        self.text_update_signal.emit(text)

    def update_button(self, text):
        self.button_update_signal.emit(text)

class SolveData:
    """Storage for solve data"""
    data = []  # 6 3x3 arrays of sizes, with corresponding depths
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
            entry = cls.data[cls.idx]
            cls.idx += 1
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

class Kinect:
    """Kinect camera functionality"""
    def __init__(self):
       self.device = Device(getDefaultDeviceSerialNumber())
       self.listener = FrameListener(Frame.COLOR, Frame.DEPTH)

       self.device.setColorFrameListener(self.listener)
       self.device.setIrAndDepthFrameListener(self.listener)
    def start(self):
        self.device.start()

    def get_kinect_frame(self):
        """Gets both RGB and Depth frame"""
        print("    Getting frame in kinect")
        frame = self.listener.waitForNewFrame()
        print("    Frame was got")
        return frame

    def stop(self):
        self.stop()

