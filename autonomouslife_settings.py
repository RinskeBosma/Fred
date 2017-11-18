from naoqi import ALProxy
from naoip import NAOIP
autolife = ALProxy("ALAutonomousLife", NAOIP, 9559)
print autolife.getState()

autolife.setState("interactive")
print autolife.getState()

#### the autonomous life states are: solitary, interactive, disabled, safeguard
#### interactive state is only entered when an interactive activity is focused
