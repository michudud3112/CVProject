import cv2

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0) #Init the cam

    def get_frame(self):
        ret, frame = self.cap.read() #Get a frame
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            return frame
        return None

    def release(self):
        self.cap.release()

    def handle_captured(self,frame):
        print(frame)
