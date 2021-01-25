from requests import get

res = get('https://www.hwbox.gr/news.html')

print(res.content)