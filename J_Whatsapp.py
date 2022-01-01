import pywhatkit
import subprocess
import pyttsx3
import json
import speech_recognition as sr
import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query



speak("Enter phone number with country code")
number1 = input("Phone number with country code(ex. India:+91 9423xxxx): ")
msg = input("The text you want to send: ")
print("Enter time in 24 hours format")
time1 = int(input("Hours: "))
time2 = int(input("Minutes: "))
speak("Your message will be sent at your given time.")
pywhatkit.sendwhatmsg(number1, msg, time1, time2)
speak("Message Sent!")
print("Message Sent!")
