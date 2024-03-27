import os.path
import time
import requests
import threading


def download_image_thread(url_thread):
    if not os.path.exists("images"):
        os.mkdir("images")
    start_time = time.time()
    name = url_thread.split("/")[-1]
    resp = requests.get(url_thread)
    if resp.status_code == 200:
        with open(f"images\\{name}", "wb") as file:
            file.write(resp.content)
    print(
        f"Многопоточный:({name}): время скачивания изображения = {time.time() - start_time:.2f} сек."
    )


list_url = [
    "https://fikiwiki.com/uploads/posts/2022-02/1644974196_32-fikiwiki-com-p-yezhiki-krasivie-kartinki-35.png",
    "https://i.pinimg.com/originals/18/a6/a3/18a6a35b02b03cf77f2bc2adaac4565f.jpg",
]

threads = []
start_time_all = time.time()
for url in list_url:
    thread = threading.Thread(target=download_image_thread, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print(
    f"Многопоточный: ИТОГО = {round(time.time() - start_time_all, 2)} сек.\n"
)
