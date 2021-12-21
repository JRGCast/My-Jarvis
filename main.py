import pyttsx3
from decouple import config

USERNAME = config('THEUSER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('espeak')

# Set Rate
engine.setProperty('rate', 180)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
voices = engine.getProperty('voices')
print(len(voices))
for index, voice in enumerate(voices):
  print(voice, index)

engine.setProperty('voice', voices[53].id)
engine.say("Meu nome é João, muito prazer")
engine.runAndWait()

# engine.runAndWait()

print(USERNAME,BOTNAME)