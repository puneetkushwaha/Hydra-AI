# Hydra-AI

#### This is my personal voice assistant project inspired by JARVIS (Iron Man movie).  
It automates many daily computer tasks using Python and voice commands.

## Built With

<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>

## Features

- Greets the user based on time of day
- Provides current time and date
- Launches applications and websites on command
- Provides weather updates for any city
- Opens location on Google Maps and calculates distance from current location
- Shows system status (CPU, RAM usage, battery)
- Reads your Google Calendar events
- Searches Wikipedia for any person or topic
- Searches Google and YouTube for queries and plays music
- Provides top news headlines (via Times of India)
- Sends emails with subject and content by voice
- Calculates mathematical expressions
- Takes notes and saves in notepad
- Tells jokes for fun
- Shares your current IP address
- Switches between windows
- Takes screenshots with custom filenames
- Hides/unhides files in a folder
- Features a simple graphical user interface (GUI)

## API Keys Required

To use some features, you need to create and use API keys from:

- [OpenWeatherMap](https://openweathermap.org/api)
- [WolframAlpha](https://www.wolframalpha.com/)
- [Google Calendar API](https://developers.google.com/calendar/auth)

## Installation and Setup

1. Clone this repository.
2. Create a `config.py` file inside the `Jarvis/config` folder with your API keys and credentials like this:

```python
weather_api_key = "<your_openweathermap_api_key>"
email = "<your_email_address>"
email_password = "<your_email_password>"
wolframalpha_id = "<your_wolframalpha_app_id>"


Create a new Python environment (optional but recommended):

conda create -n hydraai python=3.8.5
conda activate hydraai
Install dependencies:

pip install -r requirements.txt
For Windows users, install PyAudio from the wheel file (instructions here).

Run the program:
python main.py
Enjoy your personal assistant!

Project Structure

├── driver
├── Jarvis
│   ├── config        # API keys and credentials
│   ├── features      # All assistant features (modules)
│   └── utils         # GUI images and utilities
├── __init__.py       # Feature function definitions
├── gui.ui            # GUI layout file
├── main.py           # Main entry point
├── requirements.txt  # Project dependencies
Contributing
Contributions are welcome! Feel free to open issues or pull requests to improve Hydra-AI.

License
This project is licensed under the MIT License.

Future Improvements
Add Natural Language Processing for better conversation handling

Enhance the GUI design and user experience

Add more smart features and integrations

Made with ❤️ by Puneet
