import webbrowser
import requests
# from bs4 import BeautifulSoup

urls = []
urls = ['https://google.com', 'https://www.facebook.com/', 'https://www.quora.com/']
webbrowser.register('firefox',
                    None,
                    webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
# webbrowser.get('firefox').open(url)

headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
# for url in urls:

