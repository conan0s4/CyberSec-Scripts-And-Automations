#start
from bs4 import BeautifulSoup
import requests

# https://webscraper.io/test-sites
url = input("enter url: ")

x = requests.get(url)


soup = BeautifulSoup(x.content, "html.parser")


#filter using html tags
res = soup.find_all('link')
print(res)


res1 = soup.find_all(string="user")



with open('index.html', 'r') as x :
    content = x.read()
    print(content)













