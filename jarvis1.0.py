import subprocess
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import webbrowser
import os


from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")
    else:
        speak("Good Evening Sir !")
    speak("I am your Assistant")
    speak("Jarvis 1 point o")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        # print("Please say something")
        audio = r.listen(source)
        query = r.recognize_google(audio)
        print(query)
        print("Recognizing Now .... ")
        try:
            # print("You have said :" + text1)
            print("Audio Recorded Successfully \n ")
        except Exception as e:
            print("Error :  " + str(e))
    return query


def username():
    speak("What Should i call you sir?")
    usr = takeCommand()
    speak("Welcome " + usr + "sir")
    print("Welcome sir! How can i help you")


def astname():
    speak("What would you like to call me sir")


if __name__ == '__main__':
    # clear()
    # greet()
    # username()
    r = sr.Recognizer()

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)

        # print("Please say something")
        audio = r.listen(source,phrase_time_limit=5)
        req1 = r.recognize_google(audio)
        req1 = req1.lower()
        print("Recognizing Now .... ")
        try:
            print("You have said :" + req1)
            print("Audio Recorded Successfully \n ")
        except Exception as e:
            print("Error :  " + str(e))

    # req1 = takeCommand()

    print(req1)
    # print("hello1")
    if req1 == 'youtube':
        print("hello")
        speak('Opening Youtube!')
        print("hello11")
        webbrowser.open('youtube.com')
        print("hello12")
    elif req1 == 'open instagram':
        speak('Opening Instagram!')
        webbrowser.open('https://www.instagram.com/')
    elif req1 == 'open facebook':
        speak('Opening Facebook!')
        webbrowser.open('https://www.facebook.com/')
    elif req1 == 'open mytoolstown':
        speak('Opening MyToolsTown!')
        webbrowser.open('https://mytoolstown.com/')
    elif req1 == 'open google':
        speak('Opening Google!')
        webbrowser.open('https://www.google.com/')
    elif req1 == 'adobe reader':
        speak('Opening Adobe reader!')
        subprocess.call(["C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"])
