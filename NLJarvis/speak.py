import pyttsx3


def Say(Text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")

    engine.setProperty('voices', voices[3].id)
    engine.setProperty('rate', 200)
    print("    ")
    print(f"A.I : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("   ")
