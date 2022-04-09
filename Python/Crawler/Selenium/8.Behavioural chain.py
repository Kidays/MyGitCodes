from re import A
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver_path = r'C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')
inputTag = driver.find_element_by_id('kw')
subBtn = driver.find_element_by_id('su')
actions = ActionChains(driver)
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag, 'python')
actions.click(subBtn)
actions.perform()
# click_and_hold(element)
# context_click(element)
# double_click(element)
