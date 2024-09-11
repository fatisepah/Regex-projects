import requests
from bs4 import BeautifulSoup



r = requests.get('https://www.sheypoor.com/s/iran/car/peugeot/207i-panorama-at?brandInSlug=43973', allow_redirects=False)
print(r.text)

soup=BeautifulSoup(r.text,'html.parser')
print(soup)
val=soup.find('a')
print(val)
