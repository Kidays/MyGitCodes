from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
driver_path = r'C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://baidu.com/')
# driver.implicitly_wait(5)
# driver.find_element_by_id("123214")
element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'kw')))
print(element)