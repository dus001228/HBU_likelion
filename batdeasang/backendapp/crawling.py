from selenium import webdriver
from bs4 import BeautifulSoup
import datetime


def call_menu():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome('C:/Users/user/Desktop/BackEnd PJ/chromedriver.exe', options=options)

    a=[]
    T_weekday = datetime.datetime.today().weekday()
    driver.get('https://www.hanbat.ac.kr/prog/carteGuidance/kor/sub06_030301/C1/calendar.do')
    html = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, 'html.parser')
    data_1 = soup.findAll('div',class_='obj')
    for result in data_1:
        b=result
        if(result.text != ""):
         a.append(b)
    menu = str(a[T_weekday])[17:-6]
    menu = menu.split('<br/>')
    return(menu)
