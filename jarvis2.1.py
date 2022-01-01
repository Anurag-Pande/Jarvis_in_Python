import subprocess
import pyttsx3
import json

import operator
import speech_recognition as sr
import time
import datetime
import webbrowser
import os
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pds
from pandas import ExcelWriter
from pandas import ExcelFile

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon  !")
    else:
        speak("Good Evening !")
    speak("I am your Assistant")
    ast_name = 'Jarvis 1 point o'
    speak(ast_name)
    
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


file_path = 'E:\Anurag\My_Programs\Jarvis\jarvis_database.xlsx'
newData = pds.read_excel(file_path, sheet_name='Sheet1', engine='openpyxl')
# print(newData)
#greet()
query = input('what? ')
for i in range(0, 13):
    if newData['keywords'][i] == query:
        exec(open(newData['py_file'][i]).read())
# print(newData['keywords'])
