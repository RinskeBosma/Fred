# -*- encoding: UTF-8 -*-

import sys
import math
import argparse

from naoqi import ALProxy
from naoip import NAOIP




postureProxy = ALProxy("ALRobotPosture", NAOIP, 9559)
motionProxy  = ALProxy("ALMotion", NAOIP, 9559)

postureProxy.goToPosture("StandInit", 1.0)

x  = 0
y  = 0.9
theta  = 0
motionProxy.moveTo(x, y, theta)





