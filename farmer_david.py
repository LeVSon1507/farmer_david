import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
import time as t

farmer_david = pyttsx3.init()
voice = farmer_david.getProperty("voices")
farmer_david.setProperty("voice", voice[0].id)


def speak(audio):
    print("Farmer David Says: " + audio)
    farmer_david.say(audio)
    farmer_david.runAndWait()


def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(current_time)


def welcome():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good Morning sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon sir")
    elif 18 <= hour < 24:
        speak("Good Evening sir")
    else:
        speak("Hello sir")
    speak("How can I help you sir")


def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 2
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en")
        print("Son Le: " + query)
    except sr.UnknownValueError:
        speak("I didn't catch that. Please say it again.")
        return None
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the service.")
        return None
    return query.lower()


def find_vscode_path():
    possible_paths = [
        r"C:\Program Files\Microsoft VS Code\Code.exe",
        r"C:\Program Files (x86)\Microsoft VS Code\Code.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"),
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None


def process_command():
    query = get_command()
    if query:
        if "google" in query:
            speak("What should I search, sir?")
            search = get_command()
            if search:
                url = f"https://google.com/search?q={search}"
                wb.get().open(url)
                speak(f"Here are the results for {search} on Google.")
        elif "youtube" in query:
            speak("What should I search, sir?")
            search = get_command()
            if search:
                url = f"https://youtube.com/search?q={search}"
                wb.get().open(url)
                speak(f"Here are the results for {search} on YouTube.")
        elif "open video" in query:
            video_path = r"C:\Users\TECHCARE\Downloads\debug.mp4"
            os.startfile(video_path)
            speak("Opening the video.")
        elif "open vscode" or "code" or "vscode" or "visual studio code" in query:
            vscode_path = find_vscode_path()
            if vscode_path:
                os.startfile(vscode_path)
                speak("Opening Visual Studio Code.")
            else:
                speak("Visual Studio Code is not installed on this system.")
        elif "time" in query:
            get_time()
        elif "exit" in query or "stop" in query or "quit" in query:
            speak("Goodbye, sir.")
            return False
    return True


if __name__ == "__main__":
    welcome()
    while True:
        if not process_command():
            break
        t.sleep(1)
