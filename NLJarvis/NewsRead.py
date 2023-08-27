import requests
import json
import pyttsx3
from speak import Say


def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=cf6a1f78aae34768835f4e2f1384577b",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=cf6a1f78aae34768835f4e2f1384577b",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=cf6a1f78aae34768835f4e2f1384577b",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=cf6a1f78aae34768835f4e2f1384577b",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=cf6a1f78aae34768835f4e2f1384577b",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=cf6a1f78aae34768835f4e2f1384577b"
}

    content = None
    url = None
    Say("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    Say("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        Say(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    Say("thats all")