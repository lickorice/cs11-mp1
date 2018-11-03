"""
    This contains the code and logic for the
    first gamemode, SEARCHING FOR ANAGRAMS.

    Functions in this file are used by `engine.py`
    and are not meant to be used directly by neither
    `interface.py` nor `main.py`.
"""

import random, json


def init_word(dictionary, word_count):
    """
    This method instantiates a word with its corresponding anagram list.

    :returns: (`string`) random word, (`list`) anagram list.

    :param dictionary: dictionary list to be used.
    :param word_count: total number of words in the dictionary.
    :type dictionary: list
    :type word_count: int
    """

    word_index = random.randrange(word_count)
    target_word = dictionary[word_index]
    target_list = anagrams(target_word, dictionary)
    target_list.remove(target_word)

    return target_word, target_list


def anagrams(target_word, input_dict):
    """
    This function returns a list of words given an anagram and a dictionary.

    :returns: (`list`) list of anagrams.

    :param target_word: word used to search for anagrams.
    :param input_dict: dictionary to be used to search for anagrams.
    :type target_word: string
    :type input_dict: list
    """
    target_arrangement, output_list = sorted(target_word), []
    for word in input_dict:
        if sorted(word) == target_arrangement:
            output_list.append(word)
    return output_list


if __name__ == '__main__':
    main()