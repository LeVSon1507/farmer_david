import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

farmer_david = pyttsx3.init()
voice = farmer_david.getProperty("voices")
farmer_david.setProperty("voice", voice[0].id)


def speak(audio):
    print("Farmer David Say: " + audio)
    farmer_david.say(audio)
    farmer_david.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)


def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir")
    elif hour >= 18 and hour < 24:
        speak("Good Night sir")
    speak("How can i help you sir")


def command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 2
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio, language="en")
        print("Son Le: " + query)
    except:
        print("Please repeat or typing the command")
        query = str(input("Your order is: "))
    return query


if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()
        if "google" in query:
            speak("What should I search sir?")
            search = command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here are the results for {search} on Google.")
        if "youtube" in query:
            speak("What should I search sir?")
            search = command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here are the results for {search} on Youtube.")
        elif "open video":
            meme = r""
        elif "exit" in query or "stop" in query:
            speak("Goodbye, sir.")
            break
