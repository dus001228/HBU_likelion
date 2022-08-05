from selenium import webdriver
from bs4 import BeautifulSoup
import requests

options = webdriver.ChromeOptions()
# options.add_argument("headless")

driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get('https://www.hanbat.ac.kr/prog/carteGuidance/kor/sub06_030301/C1/calendar.do')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
data_1 = soup.findAll('div',class_='obj')
a=[]
for result in data_1:
    b=result
    if(result.text != ""):
       a.append(b)

print(a[0])
