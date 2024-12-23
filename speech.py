import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Čekám na tvůj hlas...")
    while True:
        audio = recognizer.listen(source, phrase_time_limit=5)
        try:
            text = recognizer.recognize_google(audio, language='cs-CZ')
            print("Řekl jsi:", text)
        except sr.UnknownValueError:
            print("Nerozuměl jsem.")
        except sr.RequestError as e:
            print("Chyba při požadavku; {0}".format(e))
