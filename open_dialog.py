# -*- encoding: UTF-8 -*-

import sys
import math
import argparse

from naoqi import ALProxy
from naoip import NAOIP

dialogProxy = ALProxy("ALDialog", NAOIP, 9559)
behaviorProxy = ALProxy("ALBehaviorManager", NAOIP, 9559)



# print behaviorProxy.getDefaultBehaviors()
# print behaviorProxy.getInstalledBehaviors()
# print behaviorProxy.getLoadedBehaviors()

behaviorProxy.startBehavior("")
print behaviorProxy.getRunningBehaviors()
