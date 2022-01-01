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

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# where to save
SAVE_PATH = "D:/"  # to_do

#from pytube import YouTube
speak('Enter the youtube video link')
youtube_video_url = input('Enter the video link: ')
#'https://www.youtube.com/watch?v=RJ1i5-XiCgs'

try:
    speak("Please Wait. Your video is downloading")
    yt_obj = YouTube(youtube_video_url)

    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

    # download the highest quality video
    filters.get_highest_resolution().download()
    speak('Video has been downloaded. Check your drive')
    print('Video Downloaded Successfully')
except Exception as e:
    print(e)