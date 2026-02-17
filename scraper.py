#start
from bs4 import BeautifulSoup
import requests

# https://webscraper.io/test-sites
url = input("enter url: ")

x = requests.get(url)


soup = BeautifulSoup(x.content, "html.parser")


res = soup.find_all('span')
print(res)













