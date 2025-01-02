import speech_recognition as sr

recognizer = sr.Recognizer()

# Adjust the recognizer's parameters
recognizer.dynamic_energy_threshold = True  # Automatically adjust for ambient noise
recognizer.energy_threshold = 4000  # Increase if it's too sensitive
recognizer.pause_threshold = 0.8    # Wait for 0.8 seconds of silence before considering the phrase complete

with sr.Microphone() as source:
    print("Čekám na tvůj hlas...")
    # Initial adjustment for ambient noise
    print("Kalibrace pro okolní hluk...")
    recognizer.adjust_for_ambient_noise(source, duration=2)
    
    while True:
        print("Poslouchám...")
        try:
            # Remove the phrase_time_limit parameter to allow for natural speech duration
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language='cs-CZ')
            print("Řekl jsi:", text)
        except sr.UnknownValueError:
            print("Nerozuměl jsem.")
        except sr.RequestError as e:
            print("Chyba při požadavku; {0}".format(e))
