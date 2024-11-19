#Testing. Requires a Kinect 2 to be connected to the computer and for pyfreect2 to be installed

from pyfreenect2 import PyFreeNect2 as Freenect, Freenect2Device as Device, getDefaultDeviceSerialNumber
from pyfreenect2 import SyncMultiFrameListener as FrameListener

# Initialize Kinect
device = Device(getDefaultDeviceSerialNumber())
device.open()

# Set up a frame listener
listener = FrameListener()
device.set_color_listener(listener)

# Start the device
device.start()
print("Kinect is successfully initialized!")

# Stop the device after the test
device.stop()
device.close()
