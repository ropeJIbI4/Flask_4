import time
import aiohttp
import asyncio


async def download_image_async(url_async):
    start_time = time.time()
    name = url_async.split("/")[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url_async) as resp:
            if resp.status == 200:
                with open(f"images\\{name}", "wb") as file:
                    while True:
                        chunk = await resp.content.read(8192)
                        if not chunk:
                            break
                        file.write(chunk)
    print(
        f"Асинхронный:({name}): время скачивания изображения = {time.time() - start_time:.2f} сек."
    )


list_url = [
    "https://fikiwiki.com/uploads/posts/2022-02/1644974196_32-fikiwiki-com-p-yezhiki-krasivie-kartinki-35.png",
    "https://i.pinimg.com/originals/18/a6/a3/18a6a35b02b03cf77f2bc2adaac4565f.jpg",
]

start_time_all = time.time()
for url in list_url:
    asyncio.run(download_image_async(url))
print(
    f"Асинхронный: ИТОГО = {round(time.time() - start_time_all, 2)} сек.\n"
)
