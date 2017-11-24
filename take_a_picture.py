
from naoqi import ALProxy
from naoip import NAOIP
photoCaptureProxy = ALProxy("ALPhotoCapture", NAOIP, 9559)
videoDeviceProxy = ALProxy("ALVideoDevice", NAOIP, 9559)

photoCaptureProxy.setResolution(2)
photoCaptureProxy.setPictureFormat("jpg")
print photoCaptureProxy.takePictures(1, "/home/nao/recordings/cameras/", "image")

# This call returns ['/home/nao/recordings/cameras/image_0.jpg']
