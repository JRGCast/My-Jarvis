import pyttsx3

engine = pyttsx3.init('espeak')

# Set Rate
engine.setProperty('rate', 160)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
voices = engine.getProperty('voices')

voice = engine.getProperty('voice')
print(len(voices), voice)

# for index, voice in enumerate(voices):
#   print(voice, index)

engine.setProperty('voice', voices[53].id,)
# engine.say(f"Olá {USERNAME}, muito PRAZER, meu nome é {BOTNAME}")
# engine.runAndWait()