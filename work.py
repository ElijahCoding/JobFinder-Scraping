import requests
from bs4 import BeautifulSoup as BS

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

url = 'https://www.work.ua/jobs-kyiv-python/'
req = session.get(url, headers=headers)
bsObj = BS(req.content, "html.parser")
data = bsObj.prettify()

handle = open('work.html', 'w')
handle.write(str(data))
handle.close()


