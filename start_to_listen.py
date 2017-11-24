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



print peopleperceptionProxy.isFaceDetectionEnabled()
print peopleperceptionProxy.isFastModeEnabled()

peopleperceptionProxy.setMaximumDetectionRange(1)

print facedetectionProxy.getLearnedFacesList()

TimeStamp = 1
FaceInfo = 1
N = 1
Time_Filtered_Reco_Info = 1
CameraPose_InTorsoFrame = 1
CameraPose_InRobotFrame = 1
Camera_Id = 1


dataFaceDetected =[
    TimeStamp,
    [ FaceInfo[N], Time_Filtered_Reco_Info ],
    CameraPose_InTorsoFrame,
    CameraPose_InRobotFrame,
    Camera_Id
]
 

print memoryProxy.raiseEvent("FaceDetection/FaceDetected", dataFaceDetected)



