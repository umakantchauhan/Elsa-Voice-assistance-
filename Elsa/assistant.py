import time
import tkinter as tk
from tkinter import PhotoImage
import tkinter.scrolledtext as scrolledtext
import threading
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia
import random
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import re
import os
from AppOpener import open
import pyautogui
import cv2

# Initialize the speech recognition and text-to-speech engines
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


class Elsa(tk.Tk):  # Changed class name from Flash to Elsa
    def __init__(self):
        super().__init__()
        self.title("Elsa - Your Personal Voice Assistant")  # Changed the title
        self.geometry("900x900")

        # Load background image
        self.background_image = PhotoImage(file="b.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.log_text = scrolledtext.ScrolledText(self, height=20, state='disabled', wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=100, pady=100)

        self.start_button = tk.Button(self, text="Start Elsa", command=self.start_listening)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.stop_button = tk.Button(self, text="Stop Elsa", command=self.stop_listening, state='disabled')
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.is_listening = False

    def start_listening(self):
        self.start_button.config(state='disabled')
        self.stop_button.config(state='normal')
        self.is_listening = True
        thread = threading.Thread(target=self.run_elsa)
        thread.start()

    def stop_listening(self):
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')
        self.is_listening = False

    def log_message(self, message):
        self.log_text.configure(state='normal')
        self.log_text.insert(tk.END, message + '\n')
        self.log_text.configure(state='disabled')
        self.log_text.see(tk.END)

    def take_command(self):
        command = ''
        try:
            with sr.Microphone() as source:
                self.log_message('Elsa is listening...')  # Changed from Flash to Elsa
                listener.adjust_for_ambient_noise(source, duration=1)
                audio = listener.listen(source, timeout=5, phrase_time_limit=5)
                command = listener.recognize_google(audio)
                self.log_message(f'User said: {command}')
        except sr.UnknownValueError:
            pass
        return command.lower()

    def translate_text(self):
        self.talk("What would you like to translate?")
        text = self.take_command()
        print("Text to translate:", text)  # Print the text to translate
        if text:
            self.talk("What language would you like to translate it into?")
            target_language = self.take_command()
            print("Target language:", target_language)  # Print the target language
            translator = Translator()
            translation = translator.translate(text, dest=target_language)
            print("Translated text:", translation.text)  # Print the translated text
            self.talk(f"The translation is: {translation.text}")

    def calculate(self, command):
        # Extract numbers and operation from command using regular expressions
        matches = re.findall(r'\d+', command)
        numbers = [int(match) for match in matches]
        operation = None
        if '+' in command:
            operation = 'addition'
            result = sum(numbers)
        elif '-' in command:
            operation = 'subtraction'
            result = numbers[0] - sum(numbers[1:])
        elif 'multiply' in command:
            operation = 'multiplication'
            result = 1
            for num in numbers:
                result *= num
        elif 'divide' in command:
            operation = 'division'
            result = numbers[0]
            for num in numbers[1:]:
                result /= num
        else:
            self.talk("I couldn't recognize the operation.")
            return
        self.talk(f"The result of {operation} is {result}")

    def open_app(self, app_name):
        try:
            os.startfile(app_name)
            self.talk(f"Opening {app_name}")
        except Exception as e:
            self.talk(f"Failed to open {app_name}")

    def take_screenshot(self):
        try:
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")
            self.talk("Screenshot saved as screenshot.png")
        except Exception as e:
            self.talk("Failed to take screenshot")

    def take_photo(self):
        try:
            # Access the default camera (0)
            cap = cv2.VideoCapture(0)

            # Capture a single frame
            ret, frame = cap.read()

            # Save the captured frame as an image
            if ret:
                cv2.imwrite("photo.jpg", frame)
                self.talk("Photo saved as photo.jpg")
            else:
                self.talk("Failed to capture photo")

            # Release the camera
            cap.release()
        except Exception as e:
            self.talk("Failed to take photo")

    def run_elsa(self):  # Changed from Flash to Elsa
        while self.is_listening:
            command = self.take_command()
            if 'exit' in command:
                self.talk('Goodbye!')
                self.stop_listening()
            elif 'time' in command:
                current_time = datetime.datetime.now().strftime('%I:%M %p')
                self.talk('Current time is ' + current_time)
            elif 'search google for' in command:
                search_query = command.replace('search google for', '')
                self.talk(f'Searching Google for {search_query}')
                webbrowser.open_new_tab(f'https://www.google.com/search?q={search_query}')
            elif 'wikipedia' in command:
                search_query = command.replace('wikipedia', '')
                try:
                    self.talk(f'Searching Wikipedia for {search_query}')
                    result = wikipedia.summary(search_query, sentences=2)
                    self.talk(result)
                except wikipedia.exceptions.DisambiguationError as e:
                    self.talk('Can you be more specific?')
            elif 'youtube' in command:
                search_query = command.replace('youtube', '')
                self.talk(f'Playing {search_query} on YouTube')
                webbrowser.open_new_tab(f'https://www.youtube.com/results?search_query={search_query}')
            elif 'translate' in command:
                self.translate_text()
            elif 'calculate' in command:
                self.calculate(command)
            elif 'open app' in command:
                app_name = command.replace('open app', '').strip()
                self.open_app(app_name)
            elif 'take screenshot' in command:
                self.take_screenshot()
            elif 'take photo' in command:
                self.take_photo()
            else:
                self.talk("Sorry, I didn't understand that.")
            time.sleep(0.1)

    def talk(self, text):
        engine.say(text)
        engine.runAndWait()
        self.log_message(f'Elsa: {text}')  # Changed from Flash to Elsa


if __name__ == '__main__':
    app = Elsa()  # Changed from Flash to Elsa
    app.mainloop()
