import subprocess
import pyttsx3
import json
import speech_recognition as sr
import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


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


speak('Opening Instagram!')
driver.get('https://www.instagram.com/')
#speak('Type your phone number, email or username')
# time.sleep(3)

#print("Enter your phone number, email or username:")
query = '8446224407'#input()
time.sleep(3)
login = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')
login.send_keys(query)
#speak('type your password')
time.sleep(3)
password = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
#print("Enter Password:")  # ******
pw = 'onetwothreefour1234'#input()

password.send_keys(pw)
log_in = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
log_in.click()
time.sleep(3)
#not now button
driver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button').click()
time.sleep(2)
#second not now button
driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm').click()
#search button click
driver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > div.pbgfb.Di7vw > div').click()
#input
searchbox = driver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
searchbox.send_keys('a_j_pande')

searchbox.send_keys(Keys.RETURN)
time.sleep(2)
searchbox.send_keys(Keys.RETURN)
time.sleep(2)
searchbox.send_keys(Keys.RETURN)
time.sleep(2)


driver.find_element_by_class_name('_9AhH0').click()
time.sleep(4)

amount = 6
i = 1
while i <= amount:
    time.sleep(4)
    # liking the photo
    driver.find_element_by_class_name('wpO6b  ').click()
    time.sleep(3)
    # clicking the next button
    driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()

    i =i+1