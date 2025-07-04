# Elsa-Voice-assistance-
Collaboratively developed a desktop-based voice assistant with GUI using Tkinter. The assistant supports real-time voice commands for tasks like time retrieval, web and YouTube search, Wikipedia summarization, language translation, basic calculations, app launching, and capturing screenshots/photos.
# 🧠 Elsa - Your Personal Voice Assistant

Elsa is a GUI-based AI voice assistant built with Python. It listens to voice commands and performs a wide range of actions like searching the web, translating text, taking screenshots/photos, performing calculations, opening apps, and more – all from a slick tkinter interface.

![Elsa UI](screenshot.png) <!-- Optional image if you have GUI screenshot -->

## 🛠 Features

- 🎤 **Voice Interaction** with Google Speech Recognition
- 💬 **Text-to-Speech** via `pyttsx3`
- 🔎 **Web Search** (Google, YouTube, Wikipedia)
- 🌐 **Language Translation** using `googletrans`
- 🧮 **Basic Math Calculations**
- 🖼 **Screenshot and Photo Capture** using `pyautogui` and `OpenCV`
- ⚙️ **App Launcher**
- ⏰ **Time Reporting**
- 🖥️ **Tkinter GUI** with scrollable logs and interactive buttons

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

**Required Libraries:**
- `speechrecognition`
- `pyttsx3`
- `tkinter` (built-in with Python)
- `requests`
- `beautifulsoup4`
- `googletrans==4.0.0-rc1`
- `wikipedia`
- `pyautogui`
- `opencv-python`
- `AppOpener`

If you're missing `PyAudio`, install it with:
```bash
pip install pipwin
pipwin install pyaudio
```

---

## 🚀 How to Run

1. Clone the repo or download the script.
2. Place an image named `b.png` in the same directory (used as background).
3. Run the assistant:

```bash
python assistant.py
```

4. Click **"Start Elsa"** to begin listening.

---

## 🎙 Sample Commands

- `"What is the time?"`
- `"Search Google for quantum computing"`
- `"Wikipedia Albert Einstein"`
- `"YouTube Lofi beats"`
- `"Translate I love you"`
- `"Calculate 45 + 67"`
- `"Open app notepad"` *(Windows only)*
- `"Take screenshot"`
- `"Take photo"`
- `"Exit"`

---

## 📁 Project Structure

```bash
├── assistant.py         # Main application
├── b.png                # Background image for GUI
├── screenshot.png       # Example screenshot (optional)
├── README.md            # This file
└── requirements.txt     # Dependencies
```

---

## 👩‍💻 Author

**Elsa** was developed by [Your Name Here] – powered by Python and a healthy dose of curiosity.

---

## 📌 Notes

- Voice recognition might be impacted by noise. Ensure a clear mic environment.
- Some commands (e.g., app opening) may be OS-specific (Windows only).
- For language translation, use language names supported by Google Translate (e.g., `"Hindi"`, `"French"`).

---

## 🧊 Future Ideas

- Add wake-word detection (e.g., “Hey Elsa”)
- Integrate ChatGPT API for more intelligent responses
- Add GUI theming/dark mode
- Add reminder and note-taking features