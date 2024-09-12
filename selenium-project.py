from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
# نصب و راه‌اندازی ChromeDriver
driver = webdriver.Chrome()

# باز کردن صفحه وب
driver.get("https://bama.ir/car/peugeot-207-at")

# صبر کردن تا صفحه کامل لود شود (مخصوصا محتوای JavaScript)
driver.implicitly_wait(10)

# دریافت محتوای HTML صفحه
html = driver.page_source
soup=BeautifulSoup(html,'html.parser')
#print(soup)
val=soup.find('a')
print(val)
# چاپ HTML کامل
#print(html)

# بستن مرورگر
#driver.quit()
