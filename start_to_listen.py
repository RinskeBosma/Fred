import sys
import math
import argparse

from naoqi import ALProxy
from naoip import NAOIP

basicawarenessProxy = ALProxy("ALBasicAwareness", NAOIP, 9559)
facedetectionProxy = ALProxy("ALFaceDetection", NAOIP, 9559)
peopleperceptionProxy = ALProxy("ALPeoplePerception", NAOIP, 9559)
memoryProxy = ALProxy("ALMemory", NAOIP, 9559)

basicawarenessProxy.startAwareness()

basicawarenessProxy.setStimulusDetectionEnabled("people", True)
basicawarenessProxy.setStimulusDetectionEnabled("sound", True)

basicawarenessProxy.setEngagementMode("SemiEngaged")
print basicawarenessProxy.getEngagementMode()


print peopleperceptionProxy.isFaceDetectionEnabled()
print peopleperceptionProxy.isFastModeEnabled()

peopleperceptionProxy.setMaximumDetectionRange(1)

print facedetectionProxy.getLearnedFacesList()

memoryProxy.raiseEvent("FaceDetected", "Rinske")




