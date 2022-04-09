from re import L
from selenium import webdriver
class Lagouspider(object):
    driver_path=r'C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver.exe'
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=Lagouspider.driver_path)
    def run(self):
        self.driver.get(self.url)
        source=self.driver.page_source
    def parse_list_page(self,source):
        self.parse_list_page(source)
if __name__=='__main__':
    spider=Lagouspider()
    spider.run()