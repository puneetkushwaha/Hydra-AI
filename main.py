from Hydra import HydraAssistant
import re
import os
import random
import pprint
import datetime
import requests
import sys
import pyjokes
import time
import pyautogui
import pywhatkit
import wolframalpha
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt, QThread
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow
from Hydra.features.gui import Ui_MainWindow
from Hydra import config

obj = HydraAssistant()

# Constants
GREETINGS = ["hello Hydra", "Hydra", "wake up Hydra", "you there Hydra", "time to work Hydra", "hey Hydra",
             "ok Hydra", "are you there Hydra"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]

EMAIL_DIC = {
    'myself': 'atharvaaingle@gmail.com',
    'my official email': 'atharvaaingle@gmail.com',
    'my second email': 'atharvaaingle@gmail.com',
    'my official mail': 'atharvaaingle@gmail.com',
    'my second mail': 'atharvaaingle@gmail.com'
}

CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]

WOLFRAM_APP_ID = config.wolframalpha_id

# Functions
def speak(text):
    obj.tts(text)

def computational_intelligence(question):
    try:
        client = wolframalpha.Client(WOLFRAM_APP_ID)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except Exception as e:
        print(f"Error in computational intelligence: {e}")
        speak("Sorry sir, I couldn't fetch the answer. Please try again.")
        return None

def startup():
    speak("Initializing Hydra")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Calibrating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = obj.tell_time()
    speak(f"Currently it is {c_time}")
    speak("I am Hydra. Online and ready sir. Please tell me how may I help you")

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
        self.screenshot_name = None
        # Add a flag to track whether the assistant is listening
        self.is_listening = True
        # Add a counter for failed voice recognition attempts
        self.failed_attempts = 0
        # Maximum failed attempts before feedback
        self.max_failed_attempts = 3

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        startup()
        
        # Remove duplicate wish() call that causes repetition
        # wish()  # This was causing double greeting

        while True:
            if self.is_listening:
                speak("Listening...")  # Add this so user knows Hydra is ready for commands
                
            try:
                command = obj.mic_input()
                
                # Reset failed attempts counter if command is successful
                if command:
                    self.failed_attempts = 0
                else:
                    self.failed_attempts += 1
                    if self.failed_attempts >= self.max_failed_attempts:
                        speak("I'm having trouble hearing you. Please check your microphone.")
                        self.failed_attempts = 0
                    continue
                    
                command = command.lower()
                print(f"Command received: {command}")
                
                # Date
                if 'date' in command:
                    date = obj.tell_me_date()
                    print(date)
                    speak(date)

                # Time
                elif "time" in command:
                    time_c = obj.tell_time()
                    print(time_c)
                    speak(f"Sir, the time is {time_c}")

                # Launch app
                elif 'launch' in command:
                    dict_app = {
                        'chrome': 'C:/Program Files/Google/Chrome/Application/chrome.exe'
                    }
                    app = command.split(' ', 1)[1] if len(command.split(' ', 1)) > 1 else None
                    if not app:
                        speak('Which application should I launch, sir?')
                        continue
                        
                    path = dict_app.get(app)
                    if path is None:
                        speak(f'Application path for {app} not found')
                        print(f'Application path for {app} not found')
                    else:
                        speak(f'Launching {app} for you sir!')
                        obj.launch_any_app(path_of_app=path)

                # Greetings
                elif any(greeting in command for greeting in GREETINGS):
                    speak(random.choice(GREETINGS_RES))

                # Open website
                elif 'open' in command:
                    domain = command.split(' ')[-1]
                    open_result = obj.website_opener(domain)
                    speak(f'Alright sir! Opening {domain}')
                    print(open_result)

                # Weather info
                elif 'weather' in command:
                    city = command.split(' ')[-1]
                    weather_res = obj.weather(city=city)
                    print(weather_res)
                    speak(weather_res)

                # Wikipedia info
                elif 'tell me about' in command:
                    topic = command.replace('tell me about', '').strip()
                    if topic:
                        wiki_res = obj.tell_me(topic)
                        print(wiki_res)
                        speak(wiki_res)
                    else:
                        speak("Sorry sir. I couldn't load your query from my database. Please try again")

                # News headlines
                elif "buzzing" in command or "news" in command or "headlines" in command:
                    news_res = obj.news()
                    speak('Source: The Times Of India')
                    speak('Today\'s Headlines are..')
                    for index, articles in enumerate(news_res):
                        pprint.pprint(articles['title'])
                        speak(articles['title'])
                        if index == len(news_res) - 2:
                            break
                    speak('These were the top headlines. Have a nice day sir!')

                # Google search
                elif 'search google for' in command:
                    obj.search_anything_google(command)

                # Play music
                elif "play music" in command or "hit some music" in command:
                    music_dir = "F://Songs//Imagine_Dragons"
                    if os.path.exists(music_dir):
                        songs = os.listdir(music_dir)
                        # Play first song only for demo, or else all songs start at once which might be unwanted
                        if songs:
                            os.startfile(os.path.join(music_dir, songs[0]))
                    else:
                        speak("Music directory not found sir.")

                # Play YouTube video
                elif 'youtube' in command:
                    try:
                        video = command.split(' ', 1)[1]
                        speak(f"Okay sir, playing {video} on YouTube")
                        pywhatkit.playonyt(video)
                    except IndexError:
                        speak("Please specify the video to play on YouTube sir.")

                # Send email
                elif "email" in command or "send email" in command:
                    sender_email = config.email
                    sender_password = config.email_password
                    try:
                        speak("Whom do you want to email sir?")
                        recipient = obj.mic_input()
                        receiver_email = EMAIL_DIC.get(recipient.lower() if recipient else "")
                        if receiver_email:
                            speak("What is the subject sir?")
                            subject = obj.mic_input()
                            speak("What should I say?")
                            message = obj.mic_input()
                            msg = 'Subject: {}\n\n{}'.format(subject, message)
                            obj.send_mail(sender_email, sender_password,
                                        receiver_email, msg)
                            speak("Email has been successfully sent")
                            time.sleep(2)
                        else:
                            speak("I couldn't find the requested person's email in my database. Please try again with a different name")
                    except Exception as e:
                        print(f"Email sending error: {e}")
                        speak("Sorry sir. Couldn't send your mail. Please try again")

                # WolframAlpha questions
                elif "calculate" in command or "what is" in command or "who is" in command:
                    answer = computational_intelligence(command)
                    if answer:
                        speak(answer)

                # Calendar events
                elif any(phrase in command for phrase in CALENDAR_STRS):
                    obj.google_calendar_events(command)

                # Take notes
                elif ("make a note" in command) or ("write this down" in command) or ("remember this" in command):
                    speak("What would you like me to write down?")
                    note_text = obj.mic_input()
                    obj.take_note(note_text)
                    speak("I've made a note of that")

                # Close notepad
                elif "close the note" in command or "close notepad" in command:
                    speak("Okay sir, closing notepad")
                    os.system("taskkill /f /im notepad++.exe")

                # Tell joke
                elif "joke" in command:
                    joke = pyjokes.get_joke()
                    print(joke)
                    speak(joke)

                # System commands
                elif "system" in command or "shutdown" in command:
                    speak("Do you want to shutdown, restart, or log off?")
                    ans = obj.mic_input()
                    if ans:
                        if "shutdown" in ans:
                            speak("Shutting down the system")
                            os.system("shutdown /s /t 5")
                        elif "restart" in ans:
                            speak("Restarting the system")
                            os.system("shutdown /r /t 5")
                        elif "log off" in ans:
                            speak("Logging off the system")
                            os.system("shutdown /l")
                        else:
                            speak("Command cancelled")
                    else:
                        speak("I didn't catch that. Command cancelled.")

                # Screenshot
                elif "screenshot" in command or "take screenshot" in command or "capture screen" in command:
                    self.screenshot_name = f"screenshot_{random.randint(1000,9999)}.png"
                    img = pyautogui.screenshot()
                    img.save(self.screenshot_name)
                    speak("Screenshot taken and saved, sir")

                # Show screenshot
                elif "show me the screenshot" in command:
                    if self.screenshot_name and os.path.exists(self.screenshot_name):
                        speak("Here is the screenshot you asked for sir")
                        img = Image.open(self.screenshot_name)
                        img.show()
                    else:
                        speak("Sorry sir, no screenshot is available currently")

                # Volume controls
                elif "volume up" in command:
                    pyautogui.press("volumeup")
                    speak("Volume increased")

                elif "volume down" in command:
                    pyautogui.press("volumedown")
                    speak("Volume decreased")

                elif "mute" in command:
                    pyautogui.press("volumemute")
                    speak("Volume muted")

                # Stop listening
                elif "stop listening" in command or "go to sleep" in command or "sleep" in command:
                    speak("Going to sleep sir, call me anytime you need me")
                    self.is_listening = False
                    # Instead of breaking, set listening mode to false
                    # This way we can still wake up Hydra later
                    
                # Wake up
                elif "wake up" in command and not self.is_listening:
                    speak("I'm awake sir. How can I help you?")
                    self.is_listening = True

                # Exit Hydra
                elif "exit" in command or "quit" in command:
                    speak("Shutting down Hydra. Have a nice day sir!")
                    sys.exit()

                # If command not recognized
                else:
                    speak("I did not understand that command, sir. Could you please repeat or try something else?")
                    
            except Exception as e:
                print(f"Error in TaskExecution: {e}")
                speak("Sorry sir, I encountered an error. Please try again.")

startExecution = MainThread()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Hydra = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Hydra)
    Hydra.show()
    startExecution.start()
    sys.exit(app.exec_())