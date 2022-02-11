from parser import Parser
from downloader import Downloader
import csv

parser = Parser()
downloader = Downloader()


def get_last_comic_id():
    with open("comics\\INDEX.csv", "r") as index_csv:
        reader = csv.reader(index_csv)
        lines = [line for line in reader]
        last_added_line = lines[-1]

        if last_added_line[0].isdigit():
            return int(last_added_line[0])

        return 0


def download_comic_from_id(comic_id):
    parser.set_comic_webpage(comic_id)
    title = parser.get_comic_title().encode("ascii", "ignore").decode()  # Ignores weird unicode characters.
    image_url = parser.get_comic_image_url()
    downloader.download_comic(comic_id, title, image_url)


def main():
    comic_id = get_last_comic_id() + 1
    while comic_id <= 2579:  # Comic 2579 was the most recent during the writing of this program.
        try:
            download_comic_from_id(comic_id)
        except:
            pass  # No errors are handled in this block because only comics with an interactive element cause errors,
            # and therefore cannot be downloaded in this way.

        comic_id += 1


if __name__ == "__main__":
    main()
