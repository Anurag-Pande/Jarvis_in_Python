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


speak('Opening MyToolsTown!')
	driver.get('https://mytoolstown.com/')
	speak('Do you have a account on MyToolsTown')
	ans = takeCommand().lower()
	if (ans == 'yes'):  # login
		speak('oh great now just login to the site')
		driver.find_element_by_css_selector('#navbarColor01 > ul > li:nth-child(7) > a > b').click()

		driver.find_element_by_xpath('//*[@id="navbarColor01"]/ul/li[7]/button').click()
		speak("Type your username or email address")
		username = input()
		driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)

		speak('Type your password')
		tools_pw = input()
		driver.find_element_by_xpath('//*[@id="password"]').send_keys(tools_pw)

		driver.find_element_by_id('loginbtn').click()

	elif (ans == 'no'):  # sign up
		driver.find_element_by_css_selector('#navbarColor01 > ul > li:nth-child(6) > a > b').click()
		speak("Create your username")
		username = input()
		driver.find_element_by_id('username')  # 12asd12asd12s  anurag2211

		speak('Type your email Address')
		e_mail = input()
		driver.find_element_by_xpath('//*[@id="email"]').send_keys(e_mail)

		speak('Create and type your password')
		tools_pw = input()

		driver.find_element_by_xpath('//*[@id="password"]').send_keys(tools_pw)
		driver.find_element_by_xpath('//*[@id="rpassword"]').send_keys(tools_pw)