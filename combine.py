import speech_recognition as sr
import subprocess
import pyttsx3

kameraFile = open('kamera.txt', 'r')
teleskopFile = open('teleskop.txt', 'r')

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Set up the speech recognition
r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    # Adjust the recognizer sensitivity to ambient noise and record audio
    r.adjust_for_ambient_noise(source)
    print("Sebutkan perintah!")
    audio = r.listen(source)

# Try to recognize the speech and run the appropriate command
try:
    text = r.recognize_google(audio, language='id-ID')
    print(f"Perintah: {text}")
    kamera = kameraFile.read()
    teleskop = teleskopFile.read()
    engine.setProperty('volume', 1.0)
    engine.setProperty('rate', 120)
    if text == "Apa itu kamera":
        engine.say(kamera)
    else :
        engine.say(teleskop)    
    engine.runAndWait()
    if "open" in text:
        # Split the text to get the app name
        app_name = text.split("open")[-1].strip()
        subprocess.run(["open", "-a", app_name])
    elif "calculate" in text:
        # Split the text to get the calculation
        calculation = text.split("calculate")[-1].strip()
        result = eval(calculation)
        print(f"Result: {result}")
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Error processing request: {0}".format(e))
