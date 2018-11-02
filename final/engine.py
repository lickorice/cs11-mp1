"""
    This is the main .py file for the game engine.

    developed by Carlos Panganiban, 2018
    github.com/lickorice | @cgpanganiban
"""

import json, player
from gamemodes import anagram, combine

with open('config/cfg_general.json') as ofile:
    cfg_general = json.load(ofile)

current_dictionary = []
current_word_count = 0
current_player = 0

def init_dictionary(filename):
    """
    This function initializes the game's dictionary given a filename.
    """
    global current_dictionary, current_word_count
    try:
        with open(filename, 'r') as f:
            current_dictionary = [line.rstrip() for line in f.readlines()]
    except FileNotFoundError:
        return False
    current_word_count= len(current_dictionary)
    return True


def anagram_init():
    """This function starts the anagram game."""
    global current_player
    current_player = player.Player()
    return anagram.init_word(current_dictionary, current_word_count)


def anagram_correct():
    """This function increments the number of words solved by the player."""
    global current_player
    current_player.words_solved += 1


def anagram_end():
    """This function returns the number of words solved by the player."""
    global current_player
    return current_player.words_solved


def main():
    print("You are running the debug version of engine.py.")
    if init_dictionary(cfg_general["DICTIONARY_FILE"]):
        print("Dictionary successfully loaded. {} words found.".format(current_word_count))
    else:
        print("Dictionary failed to load. Exiting application...")
        

if __name__ == '__main__':
    main()