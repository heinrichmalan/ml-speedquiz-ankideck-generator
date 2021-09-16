# MapleLegends Speed Quiz Anki Deck Generator

### Description

The MapleStory private server MapleLegends has a summer event. One aspect of this event is a quiz where the player is shown an image which could be a monster, item or an NPC, and they have to answer in 12 seconds.

This program creates a Flash Card Deck which can be used to study the prompts and their answers. It's based on a cheat-sheet located here [https://docs.google.com/spreadsheets/d/e/2PACX-1vRgw-mX_j0fMrk326-gniQqMXwM5n4gPvkfVtfqbMAGLnkFNlh4bVQhIJc8jX_3melXd-m-YmaPGC-9](https://docs.google.com/spreadsheets/d/e/2PACX-1vRgw-mX_j0fMrk326-gniQqMXwM5n4gPvkfVtfqbMAGLnkFNlh4bVQhIJc8jX_3melXd-m-YmaPGC-9). However, this cheat-sheet can be hard to use, and thus it could be nice to have some or most commited to memory.

### Requirements

- python 3

### How To Use
 1. Install requirements `pip3 install -r requirements.txt`
 2. Run `python3 deck_create.py --get_images`
 3. Open the generated `mlspeedquiz.apkg` in Anki.