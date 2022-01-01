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
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)    
        print("Unable to Recognize your voice.")  
        return "None"
     
    return query

path_driver = 'E:\Softwares\chromedriver.exe'
driver = webdriver.Chrome(path_driver)


speak('Opening Facebook!')
driver.get('https://www.facebook.com/')

fb = driver.find_element_by_xpath('//*[@id="email"]')
speak("Type your email address")
fb_details = input()
time.sleep(3)
fb.send_keys(fb_details)

fb = driver.find_element_by_xpath('//*[@id="pass"]')
speak('type your password')
fb_pw = input()
time.sleep(3)
fb.send_keys(fb_pw)

driver.find_element_by_name('login').click()