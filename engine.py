"""
    This is the .py file for the game engine.
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

    :returns: (`bool`) if the dictionary has been initialized correctly.

    :param filename: path for the dictionary (this is set in the config file).
    :type filename: string
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
    """
    This function starts the anagram game.
    
    In addition, it also returns a word (regardless of the number of anagrams)
    for the loading sequence to show.

    :returns: (`string`) temporary target word for the game, (`list`) list of anagrams.
    """
    global current_player
    current_player = player.Player()
    return anagram.init_word(current_dictionary, current_word_count)


def anagram_correct():
    """This function increments the number of words solved by the player."""
    global current_player
    current_player.words_solved += 1


def anagram_end():
    """
    This function returns the number of words solved by the player.
    
    :returns: (`int`) player's scrabble points upon game end.
    """
    global current_player
    return current_player.words_solved


def combine_init():
    """
    This function starts the combine game.
    
    In addition, it returns the string and the maximum points achievable
    using the string during the game.

    :returns: (`string`) letter pool, (`int`) maximum points.
    """
    global current_player
    current_player = player.Player()
    return combine.init_letters(current_dictionary, current_word_count)


def combine_correct(word, letter_string):
    """
    This function checks whether or not the player got the answer correctly.
    
    If the player is correct, it increments the players points, and returns
    a `True` value. Otherwise, it does nothing and returns a `False` value.
    
    :returns: (`bool`) check result.
    """
    global current_player
    if combine.check_answer(letter_string, word, current_dictionary):
        points = combine.convert_points(word)
        current_player.points += points
        return True
    else:
        return False


def combine_points():
    """
    This function returns the total points of the player.
    
    :returns: (`int`) player points.
    """
    global current_player
    return current_player.points


def combine_end():
    """
    This function returns the total points achieved by the player
    upon game end.
    
    :returns: (`int`) player points.
    """
    global current_player
    return current_player.points


if __name__ == '__main__':
    main()