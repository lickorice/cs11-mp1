"""
    This contains the code and logic for the
    first gamemode, SEARCHING FOR ANAGRAMS.

    developed by Carlos Panganiban, 2018
    github.com/lickorice | @cgpanganiban
"""

import random, json


def init_word(dictionary, word_count):
    """
    This method instantiates a word with its corresponding anagram list.
    Returns a word (string) and a word list (list)
    """

    word_index = random.randrange(word_count)
    target_word = dictionary[word_index]
    target_list = anagrams(target_word, dictionary)
    target_list.remove(target_word)

    return target_word, target_list


def anagrams(target_word, input_dict):
    """
    This function returns a list of words given an anagram and a dictionary.
    """
    target_arrangement, output_list = sorted(target_word), []
    for word in input_dict:
        if sorted(word) == target_arrangement:
            output_list.append(word)
    return output_list


# DEBUG MODE:

def main():
    print(init_word())

if __name__ == '__main__':
    main()