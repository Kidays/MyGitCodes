from selenium import webdriver
driver_path = r'C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://baidu.com/')
for cookie in driver.get_cookies():
    print(cookie)
print('-'*30)
# driver.delete_cookie(".baidu.com")
print(driver.get_cookie("BD_HOME"))  # name
driver.delete_all_cookies()