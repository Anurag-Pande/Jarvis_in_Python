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

driver.get("https://www.cars24.com/rto-vehicle-registration-details/")
time.sleep(3)
driver.find_element_by_css_selector("body > div.js-content > div._3ZOW1 > div > div > h3 > div").click()
number_plate = "MH01AC1234"
no_plate = driver.find_element_by_css_selector("body > div.js-content > div.zlSpQ > div:nth-child(2) > div > div.col-md-6.btTCl > div._2T9yt > form > div > input")
no_plate.send_keys(number_plate)
time.sleep(3)
no_plate.send_keys(Keys.ENTER)

time.sleep(3)

details = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div/ul")

print(details)