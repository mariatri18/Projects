import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition

engine = pyttsx3.init()


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def time_():
	Time=datetime.datetime.now().strftime("%H:%M:%S") #for 24 hour clock
	speak("The current time is")
	speak(Time)


def date_():
	year = datetime.datetime.now().year
	month = datetime.datetime.now().month	
	date = datetime.datetime.now().day
	speak("The current date is")
	speak(date)
	speak(month)
	speak(year)


def wishme():
	speak("Welcome back Maria!")
	time_()
	date_()

	#Greetings

	hour = datetime.datetime.now().hour

	if hour>=6 and hour<12:
		speak("Good Morning!")
	elif hour>=12 and hour<18:
		speak("Good Afternoon!")
	elif hour>18 and hour<24:
		speak("Good Evening!")
	else:
		speak("Good Night!")

	speak("Jarvis at your service, PLease tell me how can I help you today?")	

def TakeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening....")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing....")
		query = r.recognize_google(audio,'language=en-US')
		print(query)

	except Exception as e:
		print(e)
		print("Say that again please....")
		return "None"
	return query

TakeCommand()