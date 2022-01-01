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

speak('Opening google maps')
driver.get('https://www.google.com/maps/')
speak('Type the location you want to search')
loc_search = input('location to search:')
driver.find_element_by_xpath('//*[@id="searchboxinput"]').send_keys(loc_search)
driver.find_element_by_css_selector('#searchbox-searchbutton').click()
speak("You surely want to go to"+loc_search)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[5]/div[1]/div/button').click()
speak("Type your starting location")
start_loc = input('starting loc:')
driver.find_element_by_xpath('//*[@id="sb_ifc51"]/input').send_keys(start_loc)
mapvar = driver.find_element_by_css_selector('#sb_ifc52 > input')
mapvar.send_keys(Keys.RETURN)
