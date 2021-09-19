import asyncio
import aiohttp
import time

start_time = time.time()
url = 'https://api.showdiver.com/events/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

async def get_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(await resp.json())
            #print(await resp.text())




""" async def load_data():
    async with aiohttp.ClientSession() as session:
        tasks = [] """

loop = asyncio.get_event_loop()
loop.run_until_complete(get_data())
end_time = time.time()-start_time
print(f"\n Время выполнения: {end_time} секунд")



