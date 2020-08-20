import pyttsx3 #pip install pyttsx3
import datetime

engine = pyttsx3.init()
# engine.say("Good Morning")
# engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()         #function text to speech

speak("Good Morning")
