from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from http import cookiejar  # Python 2: import cookielib as cookiejar

url = "https://nos.nl/nieuws/binnenland"#"https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"

source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')

for a in soup.find_all('p'):
    print(a.text)
None
#source = requests.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen", cookies={'__hs_opt_out': 'no'}).text
#source = requests.Session().cookies.update({'__hs_opt_out': 'no'}).get(my_url)  # Automatically uses the session cookies
# s = requests.Session()
# s.cookies.set_policy(BlockAll())
# #s.cookies.update({'__hs_opt_out': 'no'})
#
# # Some more code...
# None
# #s.get(other_url)
# soup  = BeautifulSoup(s.get(my_url).text, 'lxml')
#
# print(soup.prettify())