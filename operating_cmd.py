import os
import speech_recognition as sr
import pyttsx3
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
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


#speak("Hello I am a part of jarvis and I can operate the windows command prompt for you")
#speak("So what will you like to do!")
query = takeCommand().lower()
if query == 'connect to wifi':
    os.system('cmd /k "netsh wlan connect name = "ABHISHEK PANDE" "')

elif query == 'disconnect wifi':
    os.system('cmd /k "netsh wlan disconnect interface = "Wi-Fi" " ')

elif query == 'what is my username':
    os.system('cmd /k"whoami"')

elif query == 'help':
    os.system('cmd /k "whoami/?"')

elif query == 'IP address of a site':
    #speak("Enter the website's url")
    url = input("Enter the website's url: ")
    os.system('cmd /k "nslookup"+url')

elif query == 'show me all user profiles':
    speak("showing user profiles")
    os.system('cmd /k "netsh wlan show profiles"')

elif query == 'show me star wars':
    os.system('cmd /k "netstat"')

elif query == 'jupyter notebook':
    os.system('cmd /k "jupyter notebook"')