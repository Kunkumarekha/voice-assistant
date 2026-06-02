import speech_recognition as sr
import webbrowser
import subprocess

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        command = r.recognize_google(audio).lower()
        print("You said:", command)

        if "youtube" in command:
            webbrowser.open("https://www.youtube.com")

        elif "gmail" in command or "mail" in command:
            webbrowser.open("https://mail.google.com")

        elif "google" in command:
            webbrowser.open("https://www.google.com")

        elif "calculator" in command:
            subprocess.Popen("calc.exe")  # Windows Calculator

        elif "exit" in command or "stop" in command:
            print("Stopping...")
            break

    except sr.UnknownValueError:
        print("Could not understand")

    except Exception as e:
        print("Error:", e)