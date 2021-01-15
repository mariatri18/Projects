from GoogleNews import GoogleNews
googlenews=GoogleNews()
googlenews=GoogleNews('en','d')

googlenews.search('Italy')
googlenews.getpage()

googlenews.result()
googlenews.gettext()