import aiohttp
import asyncio
import queue

async def fetch(client, url):
    async with client.get(url) as resp:
        assert resp.status == 200
        html = await resp.text()
        print(url, len(html))

async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as client:
        urls = ["http://www.baidu.com", "http://jd.com", "http://python.org", "http://taobao.com"] * 200
        await asyncio.wait([fetch(client, url) for url in urls])

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))



async def fetch(client, page):
    async with client.post(url, headers=headers, data=data) as response:
        html = await response.text()
        
        
