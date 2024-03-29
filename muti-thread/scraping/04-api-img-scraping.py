import os
import aiohttp, aiofiles
import asyncio
from decouple import config


async def img_downloader(session, img):
    # ?가 있다면 ? 단위로 자른값중 0번째로 자름
    img_name = img.split("/")[-1].split("?")[0]
    
    try:
        os.mkdir("./images")
    except:
        FileExistsError
    
    # response 에 값중 img에대한 값을 활용함
    async with session.get(img) as response:
        # json에 담긴 image 주소를 연후 local에 저장
        if response.status == 200:
            async with aiofiles.open(f"./images/{img_name}", mode="wb") as file:
                img_data = await response.read()
                await file.write(img_data)


async def fetch(session, url, i):
    print(i + 1)
    headers = {"X-Naver-Client-Id": config("NAVER_API_ID"), "X-Naver-Client-Secret": config("NAVER_API_SECRET")}
    async with session.get(url, headers=headers) as response:
        result = await response.json()
        items = result["items"]
        images = [item["link"] for item in items]
        
        print(images)
        await asyncio.gather(*[img_downloader(session, img) for img in images])


async def main():
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    keyword = "cat"
    urls = [f"{BASE_URL}?query={keyword}&display=20&start={1+ i*20}" for i in range(10)]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url, i) for i, url in enumerate(urls)])


if __name__ == "__main__":
    asyncio.run(main())