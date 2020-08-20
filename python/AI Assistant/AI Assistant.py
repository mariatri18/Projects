import pyttsx3 #pip install pyttsx3
import datetime

engine = pyttsx3.init()
# engine.say("Good Morning")
# engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()         #function text to speech

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")  #Take the current time
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

speak("Good Morning")
time()
date()
