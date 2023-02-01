import speech_recognition as sr
import subprocess

# Set up the speech recognition
r = sr.Recognizer()


mic = sr.Microphone()

with mic as source:
    # Adjust the recognizer sensitivity to ambient noise and record audio
    r.adjust_for_ambient_noise(source)
    print("Sebutkan perintah")
    audio = r.listen(source)
    

# Try to recognize the speech and run the appropriate command
try:
    text = r.recognize_google(audio, language='id-ID')
    print(f"Perintah: {text}")

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
