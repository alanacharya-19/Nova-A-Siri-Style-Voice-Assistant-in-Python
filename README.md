🧠 Nova – Siri-Like Voice Assistant in Python (Offline)

Nova is a Siri-style desktop voice assistant built using Python that can control your computer using voice commands.
It works fully offline (no paid APIs) and responds to every command with natural voice feedback, making it feel like a real assistant.

This project focuses on automation, voice control, and system interaction, not just speech recognition.

✨ What Nova Can Do

Nova can understand your voice and perform real actions on your PC:

🎙️ Talk back on every command (like Siri)

🖥️ Open and close any desktop application

🌐 Open websites (YouTube, Google, Instagram, Gmail, etc.)

💬 Send WhatsApp messages using voice

🔊 Control system volume (up, down, mute)

🔆 Control screen brightness

📝 Type into Notepad using voice dictation

❌ Close browser tabs and running apps

🔌 Shutdown, restart, or sleep the system

🕒 Answer basic questions (time, greetings, jokes)

All actions are confirmed by voice responses such as
“Opening YouTube”, “Sending message to John”, “Increasing volume”, etc.

🛠️ Technologies Used

Python 3

speech_recognition – voice input

pyttsx3 – text-to-speech (offline)

pyautogui – keyboard & mouse automation

screen_brightness_control – brightness control

Windows system commands

No internet-based AI or paid API is required.

🚀 How to Run
1. Clone the repository
git clone https://github.com/yourusername/nova-voice-assistant.git
cd nova-voice-assistant

2. Install dependencies
pip install pyttsx3 SpeechRecognition pyautogui screen-brightness-control pyaudio


If pyaudio fails on Windows, install the precompiled wheel.

3. Run Nova
python main.py


Say “hello” or “open youtube” and Nova will respond.

🧩 Project Goal

This project was built to:

Learn Python automation

Understand speech recognition & TTS

Create a realistic voice assistant without APIs

Build something practical, not just a demo

It’s ideal for students, beginners, and automation enthusiasts.

⚠️ Notes

Designed for Windows

App opening depends on system app names

WhatsApp automation works with WhatsApp Desktop

Microphone must be configured properly
