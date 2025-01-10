import cv2
from pyfreenect2 import Freenect2Device as Device, getDefaultDeviceSerialNumber
from pyfreenect2 import SyncMultiFrameListener as FrameListener, Frame
import matplotlib.pyplot as plt
# Initialize Kinect
device = Device(getDefaultDeviceSerialNumber())

# Set up a frame listener
listener = FrameListener(Frame.COLOR, Frame.DEPTH)
device.setColorFrameListener(listener)
device.setIrAndDepthFrameListener(listener)

# Start the device
device.start()
print("Kinect is successfully initialized!")

# CUBE DETECTION
# Get array of frames
frames = [None] * 10
for i in range(10):
    frames[i] = listener.waitForNewFrame()
    print("Frame %d is successfully captured!", i)

# Run detection algo (backproj)
# algo code
# import masker
# This will get us new frames, we need to remove the part of the frame that we don't need

rgb_frame = frames.getFrame(Frame.COLOR).getRGBData()
depth_frame = frames.getFrame(Frame.DEPTH).getDepthData()


# Visualize the RGB data
plt.figure()
plt.imshow(rgb_frame)
plt.title("RGB Frame")
plt.axis('off')

# Visualize the depth data
plt.figure()
plt.imshow(depth_frame, cmap='gray')
plt.title("Depth Frame")
plt.axis('off')

plt.show()
plt.close('all')

device.stop()