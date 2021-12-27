import speech_recognition as sr
from speakrelated import speak
from enginerelated import engine
from datetime import datetime

# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='pt-BR')
        print(f"You said {query}")
        if 'pare' in query:
            speak(engine, "Saindo!")
        else:
            speak(engine, "ok")
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak(engine, "Good night sir, take care!")
            else:
                speak(engine, 'Have a good day sir!')
            exit()
    except Exception:
        speak(engine, 'Desculpe, eu não entendi, pode repetir?')
        query = 'None'
    return query

take_user_input()