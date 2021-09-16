import re
import requests
import os
import sys
from typing import List


from alive_progress import alive_bar
import genanki

from anki import generate_speed_quiz_note
from anki.models import SpeedQuizNote
from spreadsheet_scraping import get_quiz_items, QuizItem, IMAGES_DIR, download_images



ARGS_MAPPER = {
    '--get_images': {
        'fn': download_images,
        'value': True
        }
}

def get_all_images():
    file_names = os.listdir(IMAGES_DIR)
    paths = [f"{IMAGES_DIR}/{fname}" for fname in file_names]

    return paths

def get_argument_values():
    args = sys.argv[1:]
    arg_vals_map = {}
    for arg in args:
        arg_and_vals = arg.split("=")
        if len(arg_vals) == 1:
            arg = arg_and_vals[0]
            arg_vals_map[arg] = True
        else:
            arg = arg_and_vals[0]
            val = arg_and_vals[1]
            arg_vals_map[arg] = val

    return arg_vals_map

if __name__ == "__main__":
    arg_vals = get_argument_values()
    quiz_items = get_quiz_items()

    if '--get_images' in arg_vals.keys():
        ARGS_MAPPER['--get_images']['fn'](quiz_items)

    quiz_deck = genanki.Deck(
        1925054185,
        "MapleLegends Speed Quiz - heinlein"
    )

    for item in quiz_items:
        note = generate_speed_quiz_note(item)
        quiz_deck.add_note(note)

    package = genanki.Package(quiz_deck)
    package.media_files = get_all_images()

    package.write_to_file('mlspeedquiz.apkg')
