import time, requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from getpass import getpass


driver = webdriver.Chrome('chromedriver')
driver.get('http://domi.seoultech.ac.kr/support/food/?foodtype=kb')

html = driver.page_source
driver.close()
soup = BeautifulSoup(html,'html.parser')

a = soup.findAll("td", limit=8)

string = a[1].get_text()

parser = string.replace('(돈육:국산)','')
parser = parser.replace('(계육:국산)','')
parser = parser.replace(',','')
parser = parser.replace('     ',' ')

print(parser)


#print(a[2].get_text())
#print(a[3].get_text())
#print(a[4].get_text())
#print(a[5].get_text())
#print(a[6].get_text())
#print(a[7].get_text())