from GoogleNews import GoogleNews
googlenews=GoogleNews()
googlenews=GoogleNews(lang='en')

googlenews.get_news('APPLE')
googlenews.search('APPLE')
googlenews.get_page(1)

googlenews.result()
googlenews.get_texts()