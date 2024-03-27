import os.path
import time
import requests


def download_image_sync(url_synchronous):

    if not os.path.exists("images"):
        os.mkdir("images")
    start_time = time.time()
    name = url_synchronous.split("/")[-1]
    resp = requests.get(url_synchronous)
    if resp.status_code == 200:
        with open(f"images\\{name}", "wb") as file:
            file.write(resp.content)
    print(
        f"Многопроцессорный:({name}): время скачивания изображения = {time.time() - start_time:.2f} сек."
    )


list_url = [
    "https://fikiwiki.com/uploads/posts/2022-02/1644974196_32-fikiwiki-com-p-yezhiki-krasivie-kartinki-35.png",
    "https://i.pinimg.com/originals/18/a6/a3/18a6a35b02b03cf77f2bc2adaac4565f.jpg",
]

start_time_all = time.time()
for url in list_url:
    download_image_sync(url)
print(
    f"Многопроцессорный: ИТОГО = {round(time.time() - start_time_all, 2)} сек.\n"
)
