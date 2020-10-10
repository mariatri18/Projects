import pyttsx3 #pip install pyttsx3 DONE
import datetime
import speech_recognition as sr #pip install SpeechRecognition DONE
import wikipedia #pip install wikipedia DONE
import smtplib
import webbrowser as wb
import os
import pyautogui # pip install pyautogui DONE
import psutil #pip install psutil DONE
import pyjokes #pip install pyjokes DONE

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

    speak("Leia is at your service. How can I help you?")  #The greet function plays every time

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")           #Speech to text recognition function
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

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.startls()
    server.login("mariatri13@gmail.com", "mariatri18")  #add email and password here
    server.sendmail(("mariatri13@gmail.com",  to), content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\Desktop") #Add whatever path do you want to save files

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)
                                            #This is the function about cpu and battery condition
    battery = psutil.sensors_battery
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
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

        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentence = 2)     #Searching to wikipedia
            speak(result)

        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receiveraddress"     #The receiver address here
                sendmail(to, content)
                speak("Email sent succesfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")

        elif "search in chrome" in query:
            speak("What should I search")
            chromepath = "C:\Program Files (x86)\...."    #Find where is your chrome path file
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")    #Chrome searching

        elif "logout" in query:
            os.system("shutdown -l")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")      #os command for restart shutdown and logout pc

        elif "restart" in query:
            os.system("shoutdown /r /t 1")

        elif "play songs" in query:
            songs_dir = "C:\Music"  #Add the music directoyry path file
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif "remember that" in query:
            speak("what shoud I remember?")
            data = takeCommand()
            speak("you said me to rember" + data)
            remember = open("data.txt", "w")    #Create the file.txt that is going to save there our files
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            rember = open("data.txt", "r")
            speak("you said me to remember that" + remember.read())

        elif "screenshot" in query:
            screenshot()        #Take a scrennshot of what you read and watch
            speak("Done!")

        elif "cpu" in query:
            cpu()

        elif "jokes" in query:
            jokes()     #Here is a fun corner
