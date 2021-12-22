from datetime import datetime

# General text to speech
def speak(engine, text):
  """ Used to speak the passed text with the engine, in this project is pyttsx3, so '.say' and '.runAndWait' is default """
  engine.say(text)
  engine.runAndWait()


# Greeting the user
def greet_user(engine, username, botname):
    """Greets the user according to the time"""
    hour = datetime.now().hour
    minutes = datetime.now().minute
    saytime = f"{username}, são {hour} horas e {minutes} minutos"
    if (hour >= 6) and (hour < 12):
        speak(engine, f"Bom dia {saytime}")
        print(hour, minutes)
    elif (hour >= 12) and (hour < 16):
        speak(engine, f"Boa tarde {saytime}")
    elif (hour >= 16) and (hour < 19):
        speak(engine, f"Boa noite {saytime}")
    speak(engine, f"Eu sou {botname}. Em que posso ser útil?")