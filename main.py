import subprocess
import pyautogui
import pyttsx3
import speech_recognition as sr
import time
import webbrowser
import os
import screen_brightness_control as sbc

pyautogui.FAILSAFE = False

engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty('volume', 0.9)
voices = engine.getProperty('voices')
for v in voices:
    if 'zira' in v.name.lower() or 'female' in v.name.lower():
        engine.setProperty('voice', v.id)
        break

def speak(text):
    print(f"Nova: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_command(timeout=7):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening.....")
        r.adjust_for_ambient_noise(source, duration=0.3)
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=6)
        except:
            return None
    try:
        return r.recognize_google(audio).lower()
    except:
        return None

def simple_reply(message):
    message = message.lower()
    if "hello" in message or "hi" in message:
        return "Hello! How are you today?"
    if "how are you" in message:
        return "I am doing great! Thanks for asking."
    if "your name" in message:
        return "I am Nova, your assistant."
    if "time" in message:
        return f"The time is {time.strftime('%I:%M %p')}"
    if "joke" in message:
        return "Why did the computer show up at work late? It had a hard drive!"
    if "weather" in message:
        return "I cannot check the weather right now, but I hope it’s sunny!"
    return "I did not understand that, try another command."

def open_whatsapp():
    speak("Opening WhatsApp")
    pyautogui.press('win')
    time.sleep(0.4)
    pyautogui.write('WhatsApp')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(3)

def search_friend(name):
    speak(f"Searching for {name}")
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(0.2)
    pyautogui.write(name)
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.5)

def send_message(msg):
    speak(f"Sending message: {msg}")
    pyautogui.write(msg)
    time.sleep(0.2)
    pyautogui.press('enter')

def control_volume(action):
    speak(f"Turning volume {action}")
    if action == "up":
        pyautogui.press('volumeup')
    elif action == "down":
        pyautogui.press('volumedown')
    elif action == "mute":
        pyautogui.press('volumemute')

def control_brightness(action):
    speak(f"Turning brightness {action}")
    try:
        current = sbc.get_brightness()[0]
        if action == "up":
            sbc.set_brightness(min(100, current + 10))
        elif action == "down":
            sbc.set_brightness(max(0, current - 10))
    except:
        speak("Brightness not supported")

def power_control(action):
    speak(f"{action.capitalize()}ing the computer")
    if action == "shutdown":
        os.system("shutdown /s /t 1")
    elif action == "restart":
        os.system("shutdown /r /t 1")
    elif action == "sleep":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def close_tab():
    speak("Closing tab")
    pyautogui.hotkey('ctrl', 'w')

def open_app(name):
    speak(f"Opening {name}")
    pyautogui.press('win')
    time.sleep(0.4)
    pyautogui.write(name)
    time.sleep(0.5)
    pyautogui.press('enter')

def close_app(name):
    speak(f"Closing {name}")
    os.system(f"taskkill /f /im {name}.exe")

def open_site(site):
    sites = {
        "youtube": "https://youtube.com",
        "facebook": "https://facebook.com",
        "instagram": "https://instagram.com",
        "gmail": "https://mail.google.com",
        "google": "https://google.com"
    }
    if site in sites:
        speak(f"Opening {site}")
        webbrowser.open(sites[site])

def notepad_typing():
    open_app("notepad")
    speak("Start dictating")
    while True:
        text = listen_command(timeout=10)
        if not text:
            continue
        if "stop writing" in text or "save file" in text:
            speak("Saving file")
            pyautogui.hotkey('ctrl', 's')
            time.sleep(0.5)
            pyautogui.write("note")
            pyautogui.press('enter')
            break
        pyautogui.write(text + " ")

def parse_command(cmd):
    if not cmd:
        return None, None
    if "brightness up" in cmd:
        return "brightness", "up"
    if "brightness down" in cmd:
        return "brightness", "down"
    if "volume up" in cmd:
        return "volume", "up"
    if "volume down" in cmd:
        return "volume", "down"
    if "mute" in cmd:
        return "volume", "mute"
    if "shutdown" in cmd or "power off" in cmd:
        return "power", "shutdown"
    if "restart" in cmd:
        return "power", "restart"
    if "sleep" in cmd:
        return "power", "sleep"
    if "close tab" in cmd:
        return "close_tab", None
    if "close" in cmd:
        name = cmd.replace("close", "").strip()
        return "close_app", name
    if "write" in cmd and "notepad" in cmd:
        return "notepad", None
    if "send" in cmd and "to" in cmd:
        parts = cmd.replace("send", "").split("to")
        if len(parts) == 2:
            return "whatsapp", (parts[1].strip(), parts[0].strip())
    if "open" in cmd:
        name = cmd.replace("open", "").strip()
        if name in ["youtube", "facebook", "instagram", "gmail", "google"]:
            return "site", name
        return "app", name
    return None, None

def main():
    speak("Nova ready")
    while True:
        cmd = listen_command()
        if not cmd:
            continue
        if cmd in ["exit", "quit", "stop"]:
            speak("Goodbye")
            break
        ctype, data = parse_command(cmd)
        if ctype == "brightness":
            control_brightness(data)
        elif ctype == "volume":
            control_volume(data)
        elif ctype == "power":
            power_control(data)
        elif ctype == "close_tab":
            close_tab()
        elif ctype == "close_app":
            close_app(data)
        elif ctype == "notepad":
            notepad_typing()
        elif ctype == "whatsapp":
            name, msg = data
            speak(f"Sending message to {name}")
            open_whatsapp()
            search_friend(name)
            send_message(msg)
        elif ctype == "app":
            open_app(data)
        elif ctype == "site":
            open_site(data)
        else:
            reply = simple_reply(cmd)
            speak(reply)

if __name__ == "__main__":
    main()
