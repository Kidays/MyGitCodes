from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
browser = webdriver.Edge()
try:
    browser.get('https://www.jd.com')
    input = browser.find_element_by_id('key')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 4)
    wait.until(ec.presence_of_all_elements_located((By.ID, 'J_goodsList')))
    print(browser.title)
    print(browser.current_url)
    print(browser.page_source)
    browser.close()
except Exception as e:
    print(e)
    browser.close()
# try:
#     browser.get('https://www.jd.com')
#     input = browser.find_elements_by_tag_name('li')
#     print(input)
#     print(len(input))
#     print(input[0].text)
#     input = browser.find_elements(By.TAG_NAME, 'ul')
#     print(input)
#     print(input[0].text)
#     browser.close()
# except Exception as e:
#     print(e)
#     browser.close()
