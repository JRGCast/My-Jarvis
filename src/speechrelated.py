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
        # if not 'exit' in query or 'stop' in query:
        #     speak(engine, 'Just a moment...')
        #     print(query)
        # else:
        #     hour = datetime.now().hour
        #     if hour >= 21 and hour < 6:
        #         speak(engine, "Good night sir, take care!")
        #     else:
        #         speak(engine, 'Have a good day sir!')
        #     exit()
    except Exception:
        print('Donnt understand')
        # speak(engine, 'Sorry, I could not understand. Could you please say that again?')
        # query = 'None'
    return query

take_user_input()