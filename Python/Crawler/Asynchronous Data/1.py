# import asyncio
# async def func():
#     print('hello world')

# result=func()

# asyncio.run(result)

#############################
# import asyncio
# async def func():
#     print('hello world!')
#     response=await asyncio.sleep(2)
#     print('Over!',response)

# asyncio.run(func())

#############################
# import asyncio

# async def others():
#     print('start')
#     await asyncio.sleep(2)
#     print('end')
#     return 'value'

# async def func():
#     print('execute inner code')
#     response1=await others()
#     print('Over!',response1)
#     response2=await others()
#     print('Over.',response2)

# asyncio.run(func())

#############################
# import asyncio

# async def func():
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
#     return 'value'

# async def main():
#     print('main start')
#     task1=asyncio.create_task(func())
#     task2=asyncio.create_task(func())
#     print('main over')
#     ret1=await task1
#     ret2=await task2
#     print(ret1,ret2)

# asyncio.run(main())
# main start>main over>1>1>2>2>value>value

#############################
# import asyncio

# async def func():
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
#     return 'value'

# async def main():
#     print('main start')
#     tasks=[asyncio.create_task(func(),name='n1'),asyncio.create_task(func(),name='n2')]
#     print('main over')
#     done,pending=await asyncio.wait(tasks,timeout=None)
#     print(done)

# asyncio.run(main())
#############################

import aiohttp
import asyncio
from asyncio.proactor_events import _ProactorBasePipeTransport
from functools import wraps

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
            'https://www.baidu.com',
            'https://www.pythonav.com'
        ]
        tasks = [asyncio.create_task(fetch(session, url))for url in url_list]
        done,pending=await asyncio.wait(tasks)
#solve raise RuntimeError('Event loop is closed') 
def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise
    return wrapper


_ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)

if __name__ == '__main__':
    asyncio.run(main())
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
