import subprocess
import pyttsx3
import operator
import speech_recognition as sr
import time
import os
import cv2
import pyglet
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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


def takeCommand():  # pane-side > div:nth-child(1) > div > div > div:nth-child(17) > div > div > div._3OvU8 > div._3vPI2 > div.zoWT4 > span > span > span
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_ibm(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


path_driver = 'E:\Softwares\chromedriver.exe'
driver = webdriver.Chrome(path_driver)

speak("Opening Telegram web")
w_url = "https://web.telegram.org/k/"
driver.get(w_url)

time.sleep(6)
#login by number
driver.find_element_by_css_selector("#auth-pages > div > div.tabs-container.auth-pages__container > div.tabs-tab.page-signQR.active > div > div.input-wrapper > button > div").click()
time.sleep(2)
speak("enter your mobile number")
phn_number = int(input())
time.sleep(2)
ph_no = driver.find_element_by_css_selector("#auth-pages > div > div.tabs-container.auth-pages__container > div.tabs-tab.page-sign.active > div > div.input-wrapper > div.input-field.input-field-phone > div.input-field-input")
time.sleep(2)
ph_no.send_keys(phn_number)
ph_no.send_keys(Keys.ENTER)

time.sleep(5)

speak("Enter the code here which you received on mobile telegram")
time.sleep(10)
speak("Login Success!")
time.sleep(1)
speak('What would like to do from the following options')
print('''1. Send message.
         2. Create a group.
         3. Create a channel.''')
speak("enter the person's name you want to send message")
name = input("Enter name (exact as you saved): ")

time.sleep(10)
tgd = driver.find_element_by_css_selector("#column-left > div > div > div.sidebar-header > div.input-search > input")
tgd.click()
tgd.send_keys(name)
time.sleep(10)
#driver.find_element_by_css_selector("#column-left > div > div > div.sidebar-header > div.sidebar-header__btn-container > div.btn-icon.sidebar-back-button.is-visible").click()

# clicked on name
'''tgd = driver.find_element_by_css_selector("#column-left > div > div > div.sidebar-header > div.input-search > input")
tgd.click()
tgd.send_keys(name)
time.sleep(10)'''

tgd.send_keys(Keys.ENTER)
time.sleep(5)
# driver.find_element_by_class_name("matched-text i0jNr").click()
# clicked on the text box
msgd = driver.find_element_by_css_selector("#column-center > div > div > div.chat-input > div > div.rows-wrapper.chat-input-wrapper > div.new-message-wrapper > div.input-message-container > div.input-message-input.scrollable.scrollable-y.i18n.no-scrollbar")
msgd.click()
msg = "hi"
for i in range(0, 1):
    msg = msg + "i"
    time.sleep(1)
    msgd.send_keys(msg)
    time.sleep(1)
    msgd.send_keys(Keys.ENTER)


















