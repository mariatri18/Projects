import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition

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

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")           #Speech to text recognition function
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizng...")
        query = r.recognize_google(audio, 'en=US')
        print(query)
    except Exception as e:
        print(e)
        speak("Say  that again please...")

        return "None"

    return query

if __name__ = "__main__":
    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()




# speak("Good Morning")
# date()
