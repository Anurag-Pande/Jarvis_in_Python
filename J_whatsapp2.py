import subprocess
import pyttsx3
import json
import random
import operator
import speech_recognition as sr
import time
import webbrowser
import os
import cv2
import numpy as np
import pyglet
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pytube import YouTube
from urllib.request import urlopen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():

    #pane-side > div:nth-child(1) > div > div > div:nth-child(17) > div > div > div._3OvU8 > div._3vPI2 > div.zoWT4 > span > span > span
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
    
    
path_driver = 'E:\Softwares\chromedriver.exe'
driver = webdriver.Chrome(path_driver)


speak("Opening Whatsapp web")
w_url = "https://web.whatsapp.com/"
driver.get(w_url)

time.sleep(3)
speak("Scan this qr code from your mobile whatsapp")



speak("enter the name you want to send message")  
name = input("Enter name (exact as you saved): ")

time.sleep(10)
wapd = driver.find_element_by_css_selector("#side > div.uwk68 > div > label > div > div._13NKt.copyable-text.selectable-text")
wapd.click()
wapd.send_keys(name)
#clicked on name
time.sleep(3)
wapd.send_keys(Keys.ENTER)
#driver.find_element_by_class_name("matched-text i0jNr").click()
#clicked on the text box
msgd = driver.find_element_by_css_selector("#main > footer > div._2BU3P.tm2tP.copyable-area > div._1SEwr > div > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
msgd.click()
msg = "hi"
for i in range (0,500):
    msg = msg + "i"
    msgd.send_keys(msg)
    time.sleep(2)
    msgd.send_keys(Keys.ENTER)
speak("All messages delivered successfully")