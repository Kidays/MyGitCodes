from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver=webdriver.Chrome(options=options)
# driver_path = r'C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver'
# driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')
# print(driver.page_source)
# driver.close()  # driver.qiut()
inputTag=driver.find_element(by=By.ID,value='kw')
inputTag.send_keys('python')
