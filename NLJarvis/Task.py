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


def weather():
    # generate your own api key from open weather
    api_key = "cd9b83f298eba06135ab892cd08d4310"
    Say("tell me which city")
    city = listen()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        current_temperature = data['main']['temp']
        current_temperature = data['main']["temp"]
        current_pressure = data['main']["pressure"]
        current_humidiy = data['main']["humidity"]
        weather_description = data['weather'][0]['description']
        r = ("In " + city + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description) + " weather")
        print(r)
        Say(r)
    else:
        Say(" City Not Found ")


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
    elif ("weather" in query or "temperature" in query):
        weather()


# Input Function


def InputExecution(tag, query):

    if "wikipedia" in tag:
        name = str(query).replace("Who is", "").replace(
            "About", "").replace("What is ", "").replace("wikipedia", "")
        import wikipedia
        result = wikipedia.summary(name, sentences=2)
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
