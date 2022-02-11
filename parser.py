from bs4 import BeautifulSoup
import requests


class Parser:

    def __init__(self):
        self.webpage = None

    def set_comic_webpage(self, number):
        url = f"https://xkcd.com/{number}/"
        self.set_webpage(url)

    def set_webpage(self, url):
        webpage = requests.get(url)
        self.webpage = BeautifulSoup(webpage.text, "html.parser")

    def get_comic_title(self):
        self.is_webpage_valid()
        title_tag = self.webpage.find_all(id="ctitle")[0]
        title = title_tag.text
        return title

    def get_comic_image_url(self):
        self.is_webpage_valid()

        image_tag = self.webpage.find_all(id="comic")[0].find("img")
        image_url = "https:" + image_tag["src"]
        return image_url

    def is_webpage_valid(self):
        if not self.webpage:
            raise Exception("attempted to parse unset webpage")
