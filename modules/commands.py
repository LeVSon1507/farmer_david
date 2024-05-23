import webbrowser as wb
import os
import shutil
import datetime

from modules.utils import speak, get_command
from modules.music import play_music
from modules.news import read_news
from modules.reminder import set_reminder
from modules.weather import get_weather


def handle_google_search():
    speak("What should I search, sir?")
    search = get_command()
    if search:
        url = f"https://google.com/search?q={search}"
        wb.get().open(url)
        speak(f"Here are the results for {search} on Google.")


def handle_youtube_search():
    speak("What should I search, sir?")
    search = get_command()
    if search:
        url = f"https://youtube.com/search?q={search}"
        wb.get().open(url)
        speak(f"Here are the results for {search} on YouTube.")


def handle_vscode_open():
    vscode_path = shutil.which("code")
    if vscode_path:
        os.startfile(vscode_path)
        speak("Opening Visual Studio Code.")
    else:
        speak("Visual Studio Code is not installed on this system.")


def handle_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(current_time)


def handle_weather():
    speak("Which city's weather would you like to know?")
    city = get_command()
    if city:
        get_weather(city)


def handle_news():
    read_news()


def handle_music():
    speak("Do you want to play local or spotify music?")
    music_query = get_command()
    if music_query:
        play_music(music_query)


def handle_random_video():
    # video_path = r"C:\Users\TECHCARE\Downloads\debug.mp4"
    video_path = r"https://www.youtube.com/watch?v=j2QWzvLxtR4"
    wb.open(video_path)
    speak("Opening the video.")


def handle_email():
    wb.get().open("https://mail.google.com")
    speak("Opening Gmail.")


def handle_facebook():
    wb.get().open("https://www.facebook.com")
    speak("Opening Facebook.")


def handle_reminder():
    speak("What should I remind you about?")
    reminder_text = get_command()
    if reminder_text:
        speak("In how many seconds?")
        duration = get_command()
        if duration:
            set_reminder(reminder_text, duration)


def handle_job_information():
    speak("What job information do you need?")
    job_query = get_command()
    if job_query:
        job_information(job_query)


def job_information(query):
    try:
        speak(f"The data for job {query} not available, sorry sir!")
    except Exception as e:
        print(f"An error occurred while fetching job information: {str(e)}")
        speak("Sorry, I couldn't fetch job information at the moment.")
