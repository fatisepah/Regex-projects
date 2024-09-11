import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

r = requests.get('https://bama.ir/car/peugeot-207-at', headers=headers)
#print(r.text)

soup=BeautifulSoup(r.text,'html.parser')
#print(soup)
val=soup.find('a')
print(val)
