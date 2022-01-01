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

speak('Opening Youtube!')
driver.get('https://www.youtube.com/')
speak('what do you want to watch')
query = takeCommand()
search1 = driver.find_element_by_id('search')
search1.send_keys(query)
search1.send_keys(Keys.RETURN)
vdo = driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string') #will open the first #video of the search
vdo.click()
