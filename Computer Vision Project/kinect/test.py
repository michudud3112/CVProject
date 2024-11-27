from pyfreenect2 import PyFreeNect2 as Freenect, Freenect2Device as Device, getDefaultDeviceSerialNumber
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

# Get a frame
frames = listener.waitForNewFrame()
print("Frame is successfully captured!")

rgb_frame = frames.getFrame(Frame.COLOR).getRGBData()
depth_frame = frames.getFrame(Frame.DEPTH).getDepthData()

print("RGB frame shape: ", rgb_frame.shape)
print("Depth frame shape: ", depth_frame.shape)

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