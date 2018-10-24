"""
    This contains the code and logic for the
    first gamemode, SEARCHING FOR ANAGRAMS.

    developed by Carlos Panganiban, 2018
    github.com/lickorice | @cgpanganiban
"""

import random
import json

with open('config/cfg_points.json') as ofile:
    cfg_points = json.load(ofile)


def start(dictionary, word_count, player):
    """
    This method starts a new game.
    """
    print("Finding a new word...")

    target_list = ""

    while len(target_list) < 4:
        word_index = random.randrange(word_count)
        target_word = dictionary[word_index]
        print(target_word)
        target_list = anagrams(target_word, dictionary)

    target_list.remove(target_word)
    original_list = target_list.copy()

    print("Search at least 3 anagrams for the following word:")
    print(target_word)
    print(target_list)

    # TODO: Time this part, instead of using a for loop.
    for i in range(10):
        if len(target_list) == 0:
            break
        answer = input("Enter answer: ")
        if answer in target_list:
            print("Correct!")
            player.words_solved += 1
            target_list.remove(answer)
        else:
            print("Huh?")

    print("You solved {} words!".format(player.words_solved))
    print("The following anagrams for {} is:".format(target_word))
    for word in original_list:
        print("\t{}".format(word))
    player.gamerecord = (1, target_word)



def anagrams(target_word, input_dict):
    """
    This function returns a list of words given an anagram and a dictionary.
    """
    target_arrangement, output_list = sorted(target_word), []
    for word in input_dict:
        if sorted(word) == target_arrangement:
            output_list.append(word)
    return output_list

