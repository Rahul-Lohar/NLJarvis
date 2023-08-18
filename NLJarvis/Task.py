import datetime
import psutil
import pyautogui
import requests
import pyjokes
from Listen import listen
from speak import Say
from Dictapp import openappweb
from Dictapp import closeappweb


def Time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    Say(time)


def Date():
    date = datetime.date.today()
    Say(date)


def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)

def screenshot():
    Say('Name of file')
    name = listen()
    img = pyautogui.screenshot()
    img.save("D:\\code\\jarvis\\NLJarvis\\Screenshots\\" + name + ".png")
    Say('Screenshot taken')







def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "day" in query:
        Day()
    elif "screenshot" in query:
        screenshot()

    


# Input Function


def InputExecution(tag, query):

    if "wikipedia" in tag:
        name = str(query).replace("Who is", "").replace(
            "About", "").replace("What is ", "").replace("wikipedia", "")
        import wikipedia
        result = wikipedia.summary(name, sentences =2)
        Say(result)

    elif "google" in tag:
        query = str(query).replace("google", "")
        query = str(query).replace("search", " ")
        import pywhatkit
        pywhatkit.search(query)

    elif "open" in query:
        from Dictapp import openappweb
        openappweb(query)
    elif "close" in query:
        from Dictapp import closeappweb
        closeappweb(query)