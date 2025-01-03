import os
import cv2
from cleaning.mask import ImageProcessor

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0) #Init the cam
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
        ret, frame = self.cap.read() #Get a frame

        if ret:
            save_path = os.path.join(self.save_dir, "temp.jpg")

            try:
                if cv2.imwrite(save_path,frame):
                    return frame
                else:
                    print(f"Failed to save image to {save_path}")
            except PermissionError:
                print(f"ERROR: No permissions to write to: {save_path}")
            except Exception as e:
                print(f"ERROR saving image: {str(e)}")

        return None

    def release(self):
        self.cap.release()

    def handle_captured(self,frame):
        #Start with cleaning.
        print("Cleaning")

        img_processor = ImageProcessor(os.path.join(self.save_dir, "temp.jpg"))

        clean, res = img_processor.process() #function call
        if clean:
            CamDat.add_data(res)

        if CamDat.get_size() == 6:
            #Solve
            valid, res = True, [1,2] #function call
            if not valid:
                print("solving failed")


class SolveDat:
    data = []

    @classmethod
    def create_data(cls, new):
        cls.data.append(new)

    @classmethod
    def get_data(cls):
        return cls.data

class CamDat:
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