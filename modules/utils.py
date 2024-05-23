import pyttsx3
import datetime
import speech_recognition as sr

farmer_david = pyttsx3.init("sapi5")
voice = farmer_david.getProperty("voices")
farmer_david.setProperty("voice", voice[0].id)


def speak(audio):
    print("Farmer David: " + audio)
    farmer_david.say(audio)
    farmer_david.runAndWait()


def welcome():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good Morning sir")
    elif 12 <= hour <= 18:
        speak("Good Afternoon sir")
    elif 18 <= hour < 24:
        speak("Good Evening sir")
    else:
        speak("Hello sir")
    speak("How can I help you sir")


def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.dynamic_energy_threshold = True
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en")
        print("Son Le: " + query)
    except sr.UnknownValueError:
        speak("I didn't catch that. Please try again.")
        return get_command()
    except sr.RequestError():
        speak("Sorry, I'm having trouble connecting to the service.")
        return None
    return query.lower()
