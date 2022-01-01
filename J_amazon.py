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

speak('Opening Amazon India')
driver.get('https://www.amazon.in/')
time.sleep(7)
speak('Type the product which you want to buy')
product = input("Product which you want ot order: ")
driver.find_element_by_css_selector('https://youtu.be/Fh-inmHAby8').send_keys(product)
driver.find_element_by_css_selector(';#nav-search-submit-button').click()
speak("Order the product which you want.")
