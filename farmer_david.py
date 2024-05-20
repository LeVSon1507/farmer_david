import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
import time as t
from dotenv import load_dotenv as env
import requests
import openai


env()
weather_api_key = os.getenv("WEATHER_API_KEY")
base_url = os.getenv("BASE_URL")

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


def get_weather(city):
    weather_api_key = "f8396a8819aebb820783ee30e99efeb1"
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
    speak(f"Setting a reminder for {reminder_text} in {duration} seconds.")
    t.sleep(duration)
    speak(f"Reminder: {reminder_text}")


def play_music():
    music_dir = (
        r"https://open.spotify.com/track/7eBsnbBBaPJuhxcoJwsK3P?si=833a61e67332488d"
    )
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, songs[0]))
    speak("Playing music.")


def read_news():
    news_api_key = "498bad955079449db68742a02e173a71"
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
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Provide a detailed job description and qualifications for the following role: {query}",
        max_tokens=150,
    )
    job_info = response.choices[0].text.strip()
    speak(job_info)


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
        elif (
            "open vscode" in query
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
        elif "play music" in query:
            play_music()
        elif "set reminder" in query:
            speak("What should I remind you about?")
            reminder_text = get_command()
            if reminder_text:
                speak("In how many seconds?")
                duration = int(get_command())
                set_reminder(reminder_text, duration)
        elif "news" in query:
            read_news()
        elif "job" in query:
            speak("What job information do you need?")
            job_query = get_command()
            if job_query:
                job_information(job_query)
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
