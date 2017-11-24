from naoqi import ALProxy
from naoip import NAOIP
tts = ALProxy("ALTextToSpeech", NAOIP, 9559)
tts.say("what's going on outside of this room?")
