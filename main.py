from src.enginerelated import engine
from decouple import config
from src.speakrelated import greet_user

USERNAME = config('THEUSER')
BOTNAME = config('BOTNAME')


greet_user(engine, USERNAME, BOTNAME)

print(USERNAME,BOTNAME)