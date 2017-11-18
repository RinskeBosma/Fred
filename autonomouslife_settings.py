from naoqi import ALProxy
from naoip import NAOIP
autolife = ALProxy("ALAutonomousLife", NAOIP, 9559)
print autolife.getState()
autolife.setState("disabled")
print autolife.getState()
