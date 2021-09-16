import os
import re
import requests
from typing import List

from alive_progress import alive_bar
from bs4 import BeautifulSoup as soup
import genanki

import functools
import operator

IMAGES_DIR = "images"

def flatten(list_):
    return functools.reduce(operator.iconcat, list_, [])

def chunked(it, chunk_size=2):
    i = 0
    incr = chunk_size
    while i < len(it):
        yield it[i:i+incr]
        i += incr

class QuizItem:
    image_url = None
    name = None

    def __init__(self, image_url, name):
        self.name = name
        self.image_url = image_url

    def image_file_name(self):
            alphanumeric = re.sub("[^a-zA-Z0-9\s]", "", self.name)
            spaces_removed = re.sub("\s", "_", alphanumeric)

            image_name = f"{spaces_removed}.png"

            return image_name

def download_images(quiz_items: List[QuizItem]):
    os.makedirs(IMAGES_DIR, exist_ok=True)

    with alive_bar(len(quiz_items)) as bar:
        for item in quiz_items:
            file_name = item.image_file_name
            file_path = f"{IMAGES_DIR}/{file_name}"
            if os.path.isfile(file_path):
                continue
            image_url = item.image_url
            res = requests.get(image_url)
            file_name = image_name_from_item(item.name)
            with open(file_path, "wb") as file:
                file.write(res.content)

            bar()

def get_page():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRgw-mX_j0fMrk326-gniQqMXwM5n4gPvkfVtfqbMAGLnkFNlh4bVQhIJc8jX_3melXd-m-YmaPGC-9"
    res = requests.get(url)

    if res.status_code == 200:
        return soup(res.content, "html.parser")
    else:
        with open("spreadsheet_scraping/sheet.html", "r") as file:
            return soup(file.read(), "html.parser")


def mapper(item_html_tuple):
    pic_td, name_td = item_html_tuple
    DR_FEEBLE_IMAGE_URL = "https://lh3.googleusercontent.com/docsubipk/ADHq2zkNdCZX_uPfQMYjzFwLW0AO5KsRaq4Zt90WtRvP5ICRen3r2XocjH-Ucjz34NFGR2TFxe8NaLXRqAj8IDrOGlMu9EL4TYcABRK_rkGnbt2wTA0"

    img = pic_td.find("img")

    if img is None:
        return None

    image_url = img.attrs['src']

    if image_url != DR_FEEBLE_IMAGE_URL:
        name = name_td.text
    else:
        name = "Dr. Feeble"

    return QuizItem(image_url, name)

def get_quiz_items():
    page = get_page()

    tables = page.find_all(class_="waffle")

    if len(tables) == 4:
        tables = tables[1:]

    all_items = list()

    for table in tables:
        tbody = table.find('tbody')
        table_rows = tbody.find_all('tr')

        table_rows = [row.find_all('td') for row in table_rows]

        pic_and_names = chunked(table_rows)

        pic_and_names = [list(zip(pics, names)) for pics, names in pic_and_names]

        pic_and_names = flatten(pic_and_names)

        quiz_items = [mapper(entry) for entry in pic_and_names]

        quiz_items = list(filter(lambda x: x is not None, quiz_items))

        all_items.extend(quiz_items)

    return all_items
