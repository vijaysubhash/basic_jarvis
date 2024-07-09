import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import webbrowser
import pywhatkit
import pyjokes
import sys


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice[1].id)
engine.setProperty('voice', voice[1].id)
engine.setProperty('rate', 150)


# Text to Speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# Take User Command
# Voice to Text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")
    except Exception as e:
        speak("Say that again please....")
        return "none"
    return query


# Wish Me Function
def wish():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello Sir! Jarvis at your service. How can I help you?")


def null():
    while True:
        query = takeCommand().lower()
        if "jarvis" in query:
            speak("ready")
            break


# speak("Hello Sir, Good Morning")
def there_exists(terms):
    for term in terms:
        if term in query:
            return True


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        # Logic building for Tasks
        if there_exists(['hi jarvis', "hello jarvis", "hey jarvis", "jarvis"]):
            wish()

        # Opening Notepad
        if there_exists(['notepad', 'open notepad']):
            path = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(path)

        # Opening Command Prompt
        if there_exists(["cmd", "command prompt", "open cmd", "open command prompt"]):
            os.system('start cmd')

        # Opening Camera
        if there_exists(["open camera", "camera", "cam", "open cam"]):
            cap = cv2.VideoCapture(0)
            while True:
                _, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey()
                if k == "q":
                    break
                cap.release()
                cv2.destroyAllWindows()

        # Playing Music
        if there_exists(["play music", "songs", "music", "play songs"]):
            music_dir = "C:\\Users\\polis\\Music"
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))
            # song = random.choice(songs)
            # os.startfile(os.path.join(music_dir, song)


        # Opening Youtube
        if there_exists(["open youtube", "youtube"]):
            webbrowser.open("www.youtube.com")

        # Searching using Google
        if there_exists(["google", "open google", "search this", "search on google"]):
            speak("Sir, What should I search for on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        # Whatsapp
        if there_exists(["play song on youtube", "songs in youtube", "play on youtube", "play this song", "play the song"]):
            song = takeCommand().lower()
            pywhatkit.playonyt(f"{song}")

        # Jokes
        if there_exists(["tell me a joke", "jokes", "random jokes"]):
            joke = pyjokes.get_joke()
            speak(joke)

        # Opening module documentation
        if there_exists(["open module documentation", "search this module", "module details"]):
            speak("Which module documentation would you like to read")
            cm = takeCommand().lower()
            webbrowser.open(f"https://pypi.org/project/{cm}")

        # Terminating the Program
        if there_exists(["quit", "close", "no thanks", "i am done", "bye"]):
            speak("Thank you Sir. I am closing my system now.")
            quit()

        speak("Do you have any other work, Sir?")





