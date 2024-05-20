import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
import winsound
import time as t
from os.path import join, dirname
from dotenv import load_dotenv
import requests

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)
weather_api_key = os.getenv("WEATHER_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")

farmer_david = pyttsx3.init()
voice = farmer_david.getProperty("voices")
farmer_david.setProperty("voice", voice[0].id)


def speak(audio):
    print("Farmer David: " + audio)
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
        speak("I didn't catch that. Please type or speak again.")
        return input("Type your command: ").lower()
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


def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5"
    base_url = f"{url}/weather?q={city}&appid={weather_api_key}&units=metric"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temp = main["temp"]
        humidity = main["humidity"]
        weather_info = f"The weather in {city} is currently {weather_desc} with a temperature of {temp}°C and humidity of {humidity}%."
        speak(weather_info)
    else:
        speak(
            "I couldn't fetch the weather information. Please check the city name or try again later."
        )


def set_reminder(reminder_text, duration):
    while True:
        try:
            duration = int(duration)
            if duration <= 0:
                raise ValueError
            break
        except ValueError:
            speak("Invalid input. Please enter a positive number for the duration.")
            duration = get_command()

    def countdown_timer():
        remaining_time = duration
        while remaining_time > 0:
            speak(f"{remaining_time} seconds remaining")
            t.sleep(1)
            remaining_time -= 1
        speak("Time's up! Reminder: " + reminder_text)
        winsound.Beep(300, 2000)

    countdown_timer()


def play_web_music():
    music_url = (
        "https://open.spotify.com/track/7eBsnbBBaPJuhxcoJwsK3P?si=833a61e67332488d"
    )
    wb.open(music_url)
    speak("Playing spotify music.")


def play_random_music():
    if "farmer_david" in os.getcwd():
        music_dir = f"{os.getcwd()}\\music\\music.mp3"
    else:
        music_dir = f"{os.getcwd()}\\farmer_david\\music\\music.mp3"

    # if not os.path.exists(music_dir):
    #     speak("Music directory not found.")
    #     return
    # music_files = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]
    # if not music_files:
    #     speak("No music files found in the music directory.")
    #     return
    # random_music = os.path.join(music_dir, random.choice(music_files))
    os.startfile(music_dir)
    speak("Playing random music.")


def play_music(music_query):
    if "spotify" in music_query:
        play_web_music()
    else:
        play_random_music()


def read_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json()["articles"]
        headlines = [article["title"] for article in articles[:5]]
        for i, headline in enumerate(headlines, 1):
            speak(f"Headline {i}: {headline}")
    else:
        speak("I couldn't fetch the news. Please try again later.")


def job_information(query):
    try:
        speak(f"The data for job {query} not available, sorry sir!")
    except Exception as e:
        print(f"An error occurred while fetching job information: {str(e)}")
        speak("Sorry, I couldn't fetch job information at the moment.")


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
            # video_path = r"C:\Users\TECHCARE\Downloads\debug.mp4"
            video_path = r"https://www.youtube.com/watch?v=j2QWzvLxtR4"
            wb.open(video_path)
            speak("Opening the video.")
        elif (
            "open code" in query
            or "code" in query
            or "vscode" in query
            or "visual studio code" in query
        ):
            vscode_path = find_vscode_path()
            if vscode_path:
                os.startfile(vscode_path)
                speak("Opening Visual Studio Code.")
            else:
                speak("Visual Studio Code is not installed on this system.")
        elif "time" in query:
            get_time()
        elif "weather" in query:
            speak("Which city's weather would you like to know?")
            city = get_command()
            if city:
                get_weather(city)
        elif "open facebook" in query:
            wb.get().open("https://www.facebook.com")
            speak("Opening Facebook.")
        elif "open gmail" in query:
            wb.get().open("https://mail.google.com")
            speak("Opening Gmail.")
        elif "music" in query:
            speak("Do you want to play local or spotify music?")
            music_query = get_command()
            if music_query:
                play_music(music_query)
        elif "set reminder" in query:
            speak("What should I remind you about?")
            reminder_text = get_command()
            if reminder_text:
                speak("In how many seconds?")
                duration = int(get_command())
                set_reminder(reminder_text, duration)
        elif "news" in query:
            read_news()
        elif any(word in query for word in ["thanks", "thank you", "love u"]):
            speak("My pleasure, do you need any other assistance from me, Son")
            continue_or_end = get_command()
            if "no" in continue_or_end:
                speak("Goodbye, sir.")
                quit()
            else:
                speak("What do you want to order?")
        elif "job" in query:
            speak("What job information do you need?")
            job_query = get_command()
            if job_query:
                job_information(job_query)
        elif any(
            word in query for word in ["exit", "goodbye", "bye-bye", "bye", "quit"]
        ):
            speak("Goodbye, sir.")
            return False
    return True


if __name__ == "__main__":
    welcome()
    while True:
        if not process_command():
            break
        t.sleep(1)
