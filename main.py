import pyttsx3
from decouple import config

USERNAME = config('THEUSER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say('Hello')
engine.runAndWait()

print(USERNAME,BOTNAME)