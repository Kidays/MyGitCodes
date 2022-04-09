from selenium import webdriver
import time
driver_path=r"C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')
# inputTag=driver.find_element_by_id('kw')
# inputTag=driver.find_element_by_name('wd')
# inputTag=driver.find_element_by_class_name('s_ipt')
# inputTag=driver.find_element_by_xpath("//input[@id='kw']")
inputTag=driver.find_element_by_css_selector('#kw')
inputTag.send_keys('python')
time.sleep(3)
inputTag.clear()
time.sleep(3)
driver.quit()
#checkbox: inputTag.click()
#select:
    # from selenium.webdriver.support.ui import Select
    # selectTag=Select(driver.find_element_by_name("xxx"))
    # selectTag.select_by_index(1)
    # selectTag.select_by_value("xxx")
    # selectTag.deselect_all()

# behavioural chain