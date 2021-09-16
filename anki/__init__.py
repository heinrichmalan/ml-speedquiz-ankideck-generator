import genanki
import html
from anki.models import SpeedQuizNote
from spreadsheet_scraping import QuizItem

def generate_random_id():
    import random; 
    return random.randrange(1 << 30, 1 << 31)

def get_note_image(item: QuizItem):
    return f'''<img src="{item.image_file_name()}">'''

def generate_speed_quiz_note(quiz_item: QuizItem):
    note = genanki.Note(
            model=SpeedQuizNote,
            fields=[get_note_image(quiz_item), quiz_item.name]
        )

    return note