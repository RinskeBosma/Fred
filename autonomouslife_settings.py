from naoqi import ALProxy
from naoip import NAOIP
autolife = ALProxy("ALAutonomousLife", NAOIP, 9559)
print autolife.getState()

autolife.setState("solitary")
print autolife.getState()

#### the autonomous life states are: solitary, interactive, disabled, safeguard
