import os
import cv2
from cleaning.mask import ImageProcessor


class Camera:
    """Main class for handling camera and related"""
    def __init__(self):
        self.cap = cv2.VideoCapture(0) #Init the cam TODO: replace with kinect

        self.save_dir = os.path.join(os.path.dirname(__file__), "imgs")
        if not os.path.exists(self.save_dir): #for issues with perms
            try:
                os.makedirs(self.save_dir)
                print(f"Created directory: {self.save_dir}")
            except PermissionError:
                print(f"ERROR: No permission to create directory {self.save_dir}")
                raise
            except Exception as e:
                print(f"ERROR creating directory: {str(e)}")
                raise

    def get_frame(self):
        """Gets a frame from camera instance"""
        ret, frame = self.cap.read() #Get a frame

        if ret:
            save_path = os.path.join(self.save_dir, "temp.jpg")

            try:
                if cv2.imwrite(save_path,frame):
                    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                else:
                    print(f"Failed to save image to {save_path}")
            except PermissionError:
                print(f"ERROR: No permissions to write to: {save_path}")
            except Exception as e:
                print(f"ERROR saving image: {str(e)}")

        return None

    def release(self):
        """Stops video capture"""
        self.cap.release()

    def handle_captured(self,frame):
        """Handles a captured frame. Invokes face detection. If 6 are found, begins solving"""
        #Start with cleaning.
        print("Cleaning")

        img_processor = ImageProcessor(os.path.join(self.save_dir, "temp.jpg"))

        clean, res = img_processor.process() #function call
        if clean:
            FaceData.add_data(res)

        if FaceData.get_size() == 6:
            print("Enough data")
            self.handle_solve()


    def handle_solve(self):
        """Invokes cube solving with detected faces"""
        print("Solving")
        data = FaceData.get_data()


class SolveData:
    """Storage for solve data"""
    data = []

    @classmethod
    def create_data(cls, new):
        cls.data.append(new)

    @classmethod
    def get_data(cls):
        return cls.data

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