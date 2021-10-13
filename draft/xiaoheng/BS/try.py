from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from http import cookiejar  # Python 2: import cookielib as cookiejar
# class BlockAll(cookiejar.CookiePolicy):
#     return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
#     netscape = True
#     rfc2965 = hide_cookie2 = False

url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"
browser = webdriver.Firefox(firefox_binary=FirefoxBinary())
browser.get(url)
#driver.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]').click()
#browser.find_element_by_xpath('//*[@class="VfPpkd-vQzf8d"]').click()
browser.find_element_by_xpath('//*[@class="VfPpkd-Jh9lGc"]').click()
#browser.find_element_by_xpath('//*[@jscontroller="soHxf"]').click()


soup = BeautifulSoup(browser.page_source, 'html.parser')
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