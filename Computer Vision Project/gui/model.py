import cv2
from cleaning.mask import ImageProcessor

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0) #Init the cam

    def get_frame(self):
        ret, frame = self.cap.read() #Get a frame
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2.imwrite("/imgs/img.png",frame)
            return frame
        return None

    def release(self):
        self.cap.release()

    def handle_captured(self,frame):
        #Start with cleaning.
        print("Cleaning")

        img_processor = ImageProcessor("./")

        clean, res = img_processor.run(input) #function call
        if clean:
            CamDat.add_data(res)

        if(CamDat.get_size() == 6):
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
        cls.data.__sizeof__()