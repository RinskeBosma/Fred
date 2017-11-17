from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "169.254.133.122", 9559)
tts.say("Hello, world!")
