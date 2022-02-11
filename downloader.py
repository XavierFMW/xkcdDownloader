import requests
import csv


class Downloader:

    def __init__(self):
        pass

    def download_comic(self, comic_id, comic_title, image_url):
        self.update_index_csv(comic_id, comic_title)
        self.download_comic_image(comic_id, image_url)

    def update_index_csv(self, comic_id, comic_title):
        with open("comics/INDEX.csv", "a", newline="") as index_csv:
            writer = csv.writer(index_csv)
            writer.writerow([comic_id, comic_title])

    def download_comic_image(self, comic_id, image_url):
        with open(f"comics\\{comic_id}{image_url[-4:]}", "wb") as image_file:
            image_webpage = requests.get(image_url)
            image_file.write(image_webpage.content)

