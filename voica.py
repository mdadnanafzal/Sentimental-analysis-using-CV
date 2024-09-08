import pyttsx3
import datetime
import speech_recognition as sr
#import wikipedia
#import webbrowser
import os
#import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    print("VoicA : " + audio)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 < hour < 12:
        speak("Good morning")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Voica! , your personal voice assistant")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User : {query}")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def name():
    speak("May i know your name")
    name_inp = takeCommand().lower()
    speak(f"Hello {name_inp}, what is in your mind?")



