import subprocess
import pyttsx3
import json
import random
import operator
import speech_recognition as sr
import time
import datetime
import webbrowser
import os
import cv2
import numpy as np
import pyglet
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from urllib.request import urlopen

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


def username():
    speak("What Should i call you sir?")
    usr = takeCommand()
    speak("Welcome " + usr)
    print("Welcome! How can i help you")


def astname():
    speak("What would you like to call me")  # incomplete


def on_draw():
    if player.source and player.source.video_format:
        player.get_texture().blit(50, 50)


if __name__ == '__main__':
    # clear()
    # greet()
    # username()
    path_driver = 'E:\Softwares\chromedriver.exe'
    driver = webdriver.Chrome(path_driver)

    req1 = takeCommand().lower()

    # print (req1)
    # print("hello1")
    if req1 == 'open youtube':
        speak('Opening Youtube!')
        driver.get('https://www.youtube.com/')
        speak('what do you want to watch')
        query = takeCommand()
        search1 = driver.find_element_by_id('search')
        search1.send_keys(query)
        search1.send_keys(Keys.RETURN)
        vdo = driver.find_element_by_xpath(
            '//*[@id="video-title"]/yt-formatted-string')  # will open the first video of the search
        vdo.click()

        # webbrowser.open('youtube.com')

    elif req1 == 'open instagram':
        speak('Opening Instagram!')
        driver.get('https://www.instagram.com/')
        speak('Type your phone number, email or username')
        # time.sleep(3)

        print("Enter your phone number, email or username:")
        query = input()
        login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        login.send_keys(query)
        speak('type your password')
        password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        print("Enter Password:")  # ******
        pw = input()

        password.send_keys(pw)
        log_in = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        log_in.click()

    elif req1 == 'open facebook':
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

    elif req1 == 'shutdown':
        speak("Do you wish to shutdown your computer ? (yes / no): ")
        yesno = takeCommand().lower()
        if yesno == 'no':
            exit()
        elif yesno == 'yes':
            os.system("shutdown /s /t 1")

    elif req1 == 'open my tools town':
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
            # webbrowser.open('https://mytoolstown.com/')

        # speak('which of the tool do you want to use which are appearing on the home page?')
        # tool_to_use = takeCommand()

    elif req1 == 'open amazon':  # think about login
        speak('Opening Amazon India')
        driver.get('https://www.amazon.in/')
        time.sleep(7)
        speak('Type the product which you want to buy')
        product = input("Product which you want ot order: ")
        driver.find_element_by_css_selector('https://youtu.be/Fh-inmHAby8').send_keys(product)
        driver.find_element_by_css_selector(';#nav-search-submit-button').click()
        speak("Order the product which you want.")


    elif req1 == 'open google':
        speak('Opening Google!')
        driver.get('https://www.google.com/')
        speak("What do you want to search?")
        search_query = takeCommand()
        s1 = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
        s1.send_keys(search_query)
        s1.send_keys(Keys.RETURN)

        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div[1]/a/h3/span').click()
    elif req1 == 'open google maps':
        speak('Opening google maps')
        driver.get('https://www.google.com/maps/')
        speak('Type the location you want to search')
        loc_search = input('location to search:')
        driver.find_element_by_xpath('//*[@id="searchboxinput"]').send_keys(loc_search)
        driver.find_element_by_css_selector('#searchbox-searchbutton').click()
        speak("You surely want to go to" + loc_search)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[5]/div[1]/div/button').click()
        speak("Type your starting location")
        start_loc = input('starting loc:')
        driver.find_element_by_xpath('//*[@id="sb_ifc51"]/input').send_keys(start_loc)
        mapvar = driver.find_element_by_css_selector('#sb_ifc52 > input')
        mapvar.send_keys(Keys.RETURN)

    elif req1 == 'open instagram bot':
        speak('Opening Instagram Bot!')
        driver.get('https://www.instagram.com/')
        speak('Type your phone number, email or username')

        print("Enter your phone number, email or username:")
        query = '8446224407'
        login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        login.send_keys(query)
        speak('type your password')
        password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        print("Enter Password:")
        pw = " "

        password.send_keys(pw)
        log_in = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        log_in.click()  # log in complete
        time.sleep(3)
        driver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button').click()
        # bot that will like all the posts of a person

        speak('Enter the username of the person which you follow')
        insta_user = ''
        ins = driver.find_element_by_css_selector(
            '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
        ins.send_keys(insta_user)
        ins.send_keys(Keys.RETURN)
        time.sleep(2)
        ins.send_keys(Keys.RETURN)
        time.sleep(2);
        ins.send_keys(Keys.RETURN)  # opened the acc.
        time.sleep(3)
        driver.find_element_by_class_name('_9AhH0').click()
        time.sleep(3)
        amount = 6
        i = 1
        while i <= amount:
            time.sleep(4)
            # liking the photo
            driver.find_element_by_class_name('wpO6b  ').click()
            time.sleep(2)
            # clicking the next button
            driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()

            i += 1


    elif req1 == 'adobe reader':
        speak('Opening Adobe reader!')
        subprocess.call(["C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"])

    elif req1 == 'How are you':
        speak('I am fine!')

    elif req1 == 'open steam':
        speak('Opening Steam')
        subprocess.call("C:\Program Files (x86)\Steam\Steam.exe")

    elif req1 == 'open goolgle chrome':
        speak('Opening Google Chrome')
        subprocess.call("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")


    elif (req1 == 'what is the date'):
        speak('Date is printed')
        today = time.strftime("%m/%d/%Y")
        today_format = datetime.datetime.strptime(today, "%m/%d/%Y")
        print(today_format)
        exp_date = str(today_format + datetime.timedelta(days=365)).split(" ")
        exp = exp_date[0]
        print(exp)

    elif req1 == 'open python compiler':
        speak('Opening PyCharm')
        subprocess.call("C:\Program Files\JetBrains\PyCharm Community Edition 2020.2.3\bin\pycharm64.exe")

    elif req1 == 'open valorant':
        speak('Opening Valorant')
        subprocess.call("C:/Riot Games/Riot Client")

    elif req1 == 'open java compiler':
        speak('Opening Eclipse')
        subprocess.call('E:\Softwares\eclipse\java-2020-09\eclipse\eclipse.exe')

    # elif(req1 == 'play a movie'or'play movie'):
    # speak('Which movie do want to play?')

    elif (req1 == 'i want to change your name' or 'change your name'):
        speak('What would you like to call me?')
        print('Listenting..')
        ast_name = takeCommand()
        speak('I am super happy with my new name')
