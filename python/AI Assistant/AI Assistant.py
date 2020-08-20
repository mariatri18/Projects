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
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")                        #Take the current month year and day
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back!")
    time()
    date()
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:          #Check the time and greet between some if functions
        speak("Good afteronoun")
    elif hour >=18 and hour <=24:
        speak("Good evening")
    else:
        speak("Good night")

    speak("Leia At your serivce. How can I help you?")  #The greet function plays every time

wishme()

# speak("Good Morning")
# time()
# date()
