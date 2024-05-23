import os
import webbrowser as wb

from modules.utils import speak


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

    os.startfile(music_dir)
    speak("Playing random music.")


def play_music(music_query):
    if "spotify" in music_query:
        play_web_music()
    elif "local" or "it's up to you" or "random" in music_query:
        play_random_music()
    else:
        speak("Sorry, I'm not sure what you want me to play. Please try again.")
