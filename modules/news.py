import requests
import os
import webbrowser as wb
from modules.utils import speak, get_command


def convert_to_int(value):
    number_words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
    return number_words.get(value, value)


def read_news():
    news_api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json()["articles"]
        headlines = [article["title"] for article in articles[:5]]
        for i, headline in enumerate(headlines, 0):
            speak(f"Headline {i+1}: {headline}")
        speak("Which headline would you like to hear in detail? (Say the number)")
        article_choice = get_command()
        try:
            article_index = convert_to_int(article_choice) - 1
            if 0 <= article_index < 5:
                selected_article = articles[article_index]
                speak(selected_article["title"])
                speak(selected_article["description"])
                speak(
                    "Would you like to open the article in your browser? (Say yes or no)"
                )
                open_article = get_command()
                if open_article and "yes" in open_article:
                    article_url = selected_article["url"]
                    wb.open(article_url)
                    speak("Opening the article.")
                else:
                    speak("Okay, no problem.")
            else:
                speak("Invalid choice. Please choose a number between 1 and 5.")
        except ValueError:
            speak("Invalid input. Please say a number.")
    else:
        speak("I couldn't fetch the news. Please try again later.")
