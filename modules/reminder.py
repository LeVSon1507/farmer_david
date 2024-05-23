import time as t
import winsound

from modules.utils import speak, get_command


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
