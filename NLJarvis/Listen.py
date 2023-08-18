
import speech_recognition as sr
from googletrans import Translator


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 4)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
    except:
        return ""
    query = str(query)
    return query.lower()


def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"you :{data}.")
    # print(f"you : {data}.")
    return data


def MicExecution():
    query = listen()
    data = TranslationHinToEng(query)
    return data


MicExecution()

