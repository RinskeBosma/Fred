from naoqi import ALProxy
from NaoIp import NAOIP
tts = ALProxy("ALTextToSpeech", NAOIP, 9559)
tts.say("Dag oma")
