import speech_recognition as sr
from dotenv import load_dotenv
from os.path import join, dirname

from modules import (
    handle_google_search,
    handle_youtube_search,
    speak,
    welcome,
    get_command,
    handle_job_information,
    handle_vscode_open,
    handle_time,
    handle_music,
    handle_news,
    handle_weather,
    handle_reminder,
    handle_email,
    handle_facebook,
    handle_random_video,
)

dotenv_path = join(dirname(__file__), ".env")
load_dotenv()

def process_command():
    query = get_command()
    if query:
        if "google" in query:
            handle_google_search()
        elif "youtube" in query:
            handle_youtube_search()
        elif "facebook" in query:
            handle_facebook()
        elif "gmail" in query:
            handle_email()
        elif "video" in query:
            handle_random_video()
        elif "open code" in query or "vscode" in query or "visual studio code" in query:
            handle_vscode_open()
        elif "time" in query:
            handle_time()
        elif "weather" in query:
            handle_weather()
        elif "news" in query:
            handle_news()
        elif "music" in query:
            handle_music()
        elif "set reminder" in query:
            handle_reminder()
        elif "job" in query:
            handle_job_information()
        elif any(word in query for word in ["thanks", "thank you", "love you"]):
            speak("My pleasure, do you need any other assistance from me, Son")
            continue_or_end = get_command()
            if "no" in continue_or_end:
                speak("Goodbye Sir!")
                quit()
            else:
                speak("What do you need?")
        elif any(
            word in query for word in ["exit", "goodbye", "bye-bye", "bye", "quit"]
        ):
            speak("Goodbye Sir!")
            return False
        else:
            speak("I don't understand. Can you please rephrase?")
    return True


if __name__ == "__main__":
    welcome()
    while True:
        if not process_command():
            break
