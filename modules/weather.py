import requests
import os
from modules.utils import speak


def get_weather(city):
    try:
        weather_api_key = os.getenv("WEATHER_API_KEY")
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

    except requests.exceptions.HTTPError as http_err:
        speak(
            "I couldn't fetch the weather information. Please check the city name or try again later."
        )
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        speak("An error occurred while fetching the weather information.")
        print(f"Other error occurred: {err}")
