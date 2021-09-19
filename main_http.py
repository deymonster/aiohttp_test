""" import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as resp:
            print(resp.status)
            print(await resp.text())


loop = asyncio.get_event_loop()
loop.run_until_complete(main()) """
import requests
from requests.api import request
from time import sleep
import time

start_time = time.time()
url = 'https://api.showdiver.com/events/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

def get_data():
    r = requests.get(url, headers=HEADERS, timeout=50)
    data = r.json()
    for item in data['results']:
        responce_event = requests.get(f"{url}{item['uuid']}")
        sleep(0.15)
        event_data = responce_event.json()
        #print(event_data['title'])

if __name__ == '__main__':
    get_data()
    end_time = time.time()-start_time
    print(f"\n Время выполнения: {end_time} секунд")

