# -*- encoding: UTF-8 -*-

import sys
import math
import argparse

from naoqi import ALProxy
from naoip import NAOIP

dialogProxy = ALProxy("ALDialog", NAOIP, 9559)
behaviorProxy = ALProxy("ALBehaviorManager", NAOIP, 9559)



print dialogProxy.getUserList()

print dialogProxy.getLoadedTopics("English")
dialogProxy.activateTopic('dlg_how_are_you')

print dialogProxy.getActivatedTopics

dialogProxy.gotoTopic('dlg_how_are_you')


dialogProxy.forceOutput()
