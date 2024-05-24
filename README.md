# Farmer David

Farmer David is a Python-based virtual assistant that can perform various tasks using speech recognition and text-to-speech functionalities.

## Features

-  **Voice Recognition**: Farmer David can understand spoken commands from the user using speech recognition.
-  **Text-to-Speech**: Farmer David can respond to user queries with spoken audio responses using text-to-speech synthesis.
-  **Weather Information**: Get the current weather conditions for a specific city.
-  **Search the Web**: Use Google or YouTube search functionalities directly through voice commands.
-  **Open Applications**: Open Visual Studio Code, Facebook, Gmail, or any other application installed on the system.
-  **Play Music**: Play local music files or open Spotify to play music online.
-  **Set Reminders**: Set reminders for specific tasks.
-  **Read News**: Fetch top headlines from various news sources.
-  **Job Information**: Retrieve detailed job descriptions and qualifications for specific roles.

### Available Commands:

-  **Google Search**: Use phrases like "Google something" or "Search for something on Google" followed by your query to perform a Google search.
-  **YouTube Search**: Use phrases like "Search something on YouTube" followed by your query to perform a YouTube search.
-  **Open Visual Studio Code**: Use phrases like "Open Visual Studio Code" or "Open Code" to launch Visual Studio Code.
-  **Open Facebook**: Use phrases like "Open Facebook" to open the Facebook website in your default web browser.
-  **Open Gmail**: Use phrases like "Open Gmail" to open the Gmail website in your default web browser.
-  **Play Music**: Use phrases like "Play local music" or "Play Spotify music" followed by your preference to play music.
-  **Set Reminder**: Use phrases like "Set a reminder" followed by the reminder message and duration in seconds to set a reminder.
-  **Get Weather**: Use phrases like "What's the weather like in [city]?" to get the current weather conditions for a specific city.
-  **Read News**: Use phrases like "Read me the news" to fetch and read the top headlines from various news sources.
-  **Get Job Information**: Use phrases like "Job information for [job title]" to retrieve detailed job descriptions and qualifications for specific roles.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/LeVSon1507/farmer_david
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   -  Create a `.env` file in the project directory.
   -  Add your API keys for OpenWeatherMap (`WEATHER_API_KEY`), News API (`NEWS_API_KEY`) to the `.env` file.

## Usage

0. Prepare venv for `farmer david` script(optional):

   Step 1:

   ```bash
   python -m venv venv
   ```

   Step 2: Activate venv
   Windows:

   ```bash
   venv\Scripts\activate
   ```

   Linux/Mac:

   ```bash
   source venv/bin/activate
   ```

1. Run the `farmer_david.py` script:

   ```bash
   python farmer_david.py
   ```

2. Follow the prompts and speak your commands to interact with Farmer David.

3. Convert .py to .exe:

   ```bash
   python -m PyInstaller main.spec --noconfirm
   ```

   or

   ```bash
   pyinstaller --onefile -w main.spec
   ```

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)
