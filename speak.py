from naoqi import ALProxy
from naoip import NAO_IP


tts = ALProxy("ALTextToSpeech", NAO_IP, 9559)
tts.say("Hello, world!")
tts.say("Nirmal stinks")
