import requests

NewsAPIKey = "734d36a3896a42aaa3f2d6bdd15f38de"

def NewsBBC():
    main_url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=" + NewsAPIKey
    open_bbc_page = requests.get(main_url).json()
    article = open_bbc_page["articles"]

    NewsResults = []

    for ar in article:
        NewsResults.append(ar["title"])
    for i in range(len(NewsResults)):
        print(i + 1, NewsResults[i])

NewsBBC()        