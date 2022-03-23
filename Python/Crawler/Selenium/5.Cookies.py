from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s=Service(executable_path=r'C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver')
browser=webdriver.Chrome(service=s)
browser.get('https://www.jd.com')
print(browser.get_cookies())
browser.add_cookie({'name':'name','value':'jd','domain':'www.jd.com'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())