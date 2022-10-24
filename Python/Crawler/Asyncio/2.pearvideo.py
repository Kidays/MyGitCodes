from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import asyncio
import aiohttp
from asyncio.proactor_events import _ProactorBasePipeTransport
from functools import wraps
import time
options = webdriver.ChromeOptions()

# 处理SSL证书错误问题
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
# 忽略无用的日志
options.add_experimental_option(
    "excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(options=options)
urls = []
video_urls = []
try:
    driver.get('https://www.pearvideo.com/category_1')
    detail_urls = driver.find_elements(
        by=By.XPATH, value='//*[@id="listvideoListUl"]/li')
    for detail_url in detail_urls:
        sub = detail_url.find_element(by=By.TAG_NAME, value='a')
        sub_url = sub.get_attribute('href')
        # print(sub_url)
        urls.append(sub_url)
    # below is incorrect:
    #     driver.get(sub_url)
    #     time.sleep(2)
    #     video_url_info=driver.find_element(by=By.XPATH,value='//*[@id="JprismPlayer"]/video')
    #     video_url=video_url_info.get_attribute('src')
    #     video_urls=video_urls.append(video_url)
    # print(urls,video_urls)
except Exception as e:
    print(e)
    driver.close()
video_urls = []
for url in urls:
    try:
        driver.get(url)
        time.sleep(3)
        video_url_info = driver.find_element(
            by=By.XPATH, value='//*[@id="JprismPlayer"]/video')
        video_url = video_url_info.get_attribute('src')
        video_urls.append(video_url)
    except Exception as e:
        print(e)
        driver.close()
print(video_urls)


async def fetch(session, url):
    print('send request:', url)
    async with session.get(url, verify_ssl=False)as response:
        text = await response.text()
        print('result', url, len(text))
        return text


async def main():
    async with aiohttp.ClientSession()as session:
        url_list = [
            'https://python.org',
            'https://www.baidu.com'
            # 'https://www.pythonav.com'
        ]
        tasks = [asyncio.create_task(fetch(session, url))for url in url_list]
        done, pending = await asyncio.wait(tasks)
# solve raise RuntimeError('Event loop is closed')


def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise
    return wrapper


_ProactorBasePipeTransport.__del__ = silence_event_loop_closed(
    _ProactorBasePipeTransport.__del__)

if __name__ == '__main__':
    asyncio.run(main())

