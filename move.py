from naoqi import ALProxy
from naoip import NAO_IP


motion = ALProxy("ALMotion", NAO_IP, 9559)
tts    = ALProxy("ALTextToSpeech", NAO_IP, 9559)
motion.moveInit()
motion.post.moveTo(0.5, 0, 0)
tts.say("I'm walking jackasses")