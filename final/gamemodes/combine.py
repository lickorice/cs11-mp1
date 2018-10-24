"""
    This contains the code and logic for the
    second gamemode, COMBINING WORDS.

    developed by Carlos Panganiban, 2018
    github.com/lickorice | @cgpanganiban
"""

import random, json

with open('config/cfg_points.json') as ofile:
    cfg_points = json.load(ofile)

cfg_points = {int(entry) : cfg_points[entry] for entry in cfg_points}

def start(dictionary, word_count, player):
    """
    This method starts a new game.
    """

    word_list = []
    for i in range(3):
        word_list.append(dictionary[random.randrange(word_count)])

    target_string = generate_string(generate_sequence(word_list))
    total_points, cur_words = max_points(target_string, dictionary), []
    print("Find words from this sequence of characters:")
    print(target_string)
    
    # TODO: also change this to some time-based element
    for i in range(10):
        answer = input("Enter word: ")
        if check_answer(target_string, answer, dictionary) and answer not in cur_words:
            points = convert_points(answer)
            cur_words.append(answer)
            print("Correct! {} points gained.".format(points))
            player.points += points
        else:
            print("Try Again!")

    print("In total, you got {} points out of".format(player.points))
    print("a possible total of {} points!".format(total_points))
    player.gamerecord = (2, target_string)


def generate_sequence(word_list):
    """
    This function returns an absolute minimum dictionary of letters required
    to form a given list of words.
    """
    alphabet = {chr(i): 0 for i in range(97, 123)}
    for word in word_list:
        character_dict = {}
        for character in word:
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1

        # resolving output alphabet:
        for character in character_dict:
            alphabet[character] = max(character_dict[character], alphabet[character])
    return alphabet


def generate_string(sequence):
    """
    Given a sequence (alphabet dictionary), generate a string of *ordered* letters.
    """
    output_str = ''
    for character in sequence:
        output_str += character*sequence[character]
    output_str = list(output_str)
    random.shuffle(output_str)
    output_str = ''.join(output_str)
    return output_str


def check_answer(sequence_str, input_str, input_dict):
    """
    This function returns a Boolean given a sequence string (sequence_str),
    an answer string (input_str), and an input dictionary (input_dict).
    """
    if input_str not in input_dict:
        return False

    sequence_list = [i for i in sequence_str]

    for character in input_str:
        if character in sequence_list:
            sequence_list.remove(character)
        else:
            return False
    return True


def convert_points(word):
    """
    This returns the scrabble points (integer) of a word (string).
    """
    output_pts = 0
    for letter in word:
        for point in cfg_points:
            if letter in cfg_points[point]:
                output_pts += point
                break
    return output_pts


def max_points(input_str, input_dict):
    """
    This returns the maximum points (integer) that you can achieve
    given a scrambled string (input_str) and a dictionary (input_dict)
    """
    output_pts, output_words = 0, []

    for _word in input_dict:
        check_list, in_dict = [i for i in input_str], True
        for _char in _word:
            if _char not in check_list:
                in_dict = False
                break
            else:
                check_list.remove(_char)
        if in_dict:
            output_words.append(_word)

    for word in output_words:
        for character in word:
            for entry in cfg_points:
                if character in cfg_points[entry]:
                    output_pts += entry
                    break
    return output_pts