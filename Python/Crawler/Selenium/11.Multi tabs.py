from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service(
    r'C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver.exe')
# driver=webdriver.Chrome(executable_path=driver_path) #old
driver = webdriver.Chrome(service=s)
driver.get('https://www.baidu.com/')
driver.execute_script("window.open('https://douban.com/')")
# print(driver.current_url)
# print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)
# print(driver.page_source)
