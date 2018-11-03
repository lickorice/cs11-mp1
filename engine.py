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

status_gameRuntime = False
status_gameMode = 0

def init_dictionary():
    """
    This function initializes the game's dictionary.
    To change the dictionary, change the directory at
    config/cfg_general.json
    """
    global current_dictionary, current_word_count
    try:
        with open(cfg_general["DICTIONARY_FILE"], 'r') as f:
            current_dictionary = [line.rstrip() for line in f.readlines()]
    except FileNotFoundError:
        return False, 0
    current_word_count= len(current_dictionary)
    return True, current_word_count


def anagrams(target_word, input_dict):
    """
    This function returns a list of words given an anagram and a dictionary.
    """
    target_arrangement, output_list = sorted(target_word), []
    for word in input_dict:
        if sorted(word) == target_arrangement:
            output_list.append(word)
    return output_list


def start_game(gamemode, _player):
    """
    This function starts a game, given the gamemode (integer) and _player (Player()).
        gamemode            |       game
        1                           SEARCHING FOR ANAGRAMS
        2                           COMBINING WORDS
    These are hardcoded, and have to be changed within the code itself.
    You also need to pass a Player object, to store the points, etc.
    """
    global status_gameRuntime, status_gameMode
    if gamemode == 1:
        print("Starting anagram search game...")
        status_gameRuntime, status_gameMode = True, 1
        anagram.start(current_dictionary, current_word_count, _player)
    elif gamemode == 2:
        print("Starting combine words game...")
        status_gameRuntime, status_gameMode = True, 2
        combine.start(current_dictionary, current_word_count, _player)
    else:
        print("Game mode invalid. Closing the game...")
        return

    print("You just finished a game.", _player.words_solved, _player.gamerecord)
    status_gameRuntime = False, 0


def main():
    print("You are running the debug version of engine.py.")
    if init_dictionary():
        print("Dictionary successfully loaded. {} words found.".format(current_word_count))
    else:
        print("Dictionary failed to load. Exiting application...")

    current_player = player.Player()

    start_game(2, current_player)

if __name__ == '__main__':
    main()