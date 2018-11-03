"""
    This contains the code and logic for the
    second gamemode, COMBINING WORDS.

    Functions in this file are used by `engine.py`
    and are not meant to be used directly by neither
    `interface.py` nor `main.py`.
"""

import random, json

with open('config/cfg_points.json') as ofile:
    cfg_points = json.load(ofile)

cfg_points = {int(entry) : cfg_points[entry] for entry in cfg_points}


def init_letters(dictionary, word_count):
    """
    This function generates a list of 16 letters that have valid 
    answers based on the dictionary.

    :returns: (`string`) string of 16 letters, (`int`) maximum points.

    :param dictionary: dictionary to be used to generate the letters.
    :param word_count: word count of the dictionary.
    :type dictionary: list
    :type word_count: int
    """

    word_list = []

    while True:
        for i in range(3):
            word_list.append(dictionary[random.randrange(word_count)])

        target_string = generate_string(generate_sequence(word_list))
        if len(target_string) == 16:
            return target_string, max_points(target_string, dictionary)
        elif len(target_string) > 16:
            target_string = target_string[:16]
            if max_points(target_string, dictionary) == 0:
                continue    
            else:
                return target_string, max_points(target_string, dictionary)
        else:
            while True:
                if len(target_string) == 16:
                    return target_string, max_points(target_string, dictionary)
                else:
                    target_string += chr(random.randint(97, 122))
                    return target_string, max_points(target_string, dictionary)


def generate_sequence(word_list):
    """
    This function generates an absolute minimum dictionary of letters required
    to form a given list of words.

    :returns: (`dict`) dictionary of letters and letter count.
      
    :param word_list: list of words to be used to generate the letters.
    :type word_list: list
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

    :returns: (`string`) a randomly generated string made from the absolute minimum letter dictionary.

    :param sequence: an absolute minimum letter dictionary produced by ``combine.generate_sequence``.
    :type sequence: dict
    """
    output_str = ''
    for character in sequence:
        output_str += character*sequence[character]
    output_list = [x for x in output_str]
    random.shuffle(output_list)
    output_str = ''
    for character in output_list:
        output_str += character
    return output_str


def check_answer(sequence_str, input_str, input_dict):
    """
    This function checks if your answer is within bounds of the
    generated string and is valid based on the dictionary.

    :returns: (`bool`) `True` or `False` if answer is correct.

    :param sequence_str: the sequence string provided by the game.
    :param input_str: the answer from the player.
    :param input_dict: the dictionary to be used.
    :type sequence_str: string
    :type input_str: string
    :type input_dict: list
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
    This converts the scrabble points of a word.

    :returns: (`int`) scrabble points.

    :param word: input word.
    :type word: string
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
    given a scrambled string (input_str) and a dictionary (input_dict).

    :returns: (`int`) maximum achievable points of the word.

    :param input_str: the generated letter pool string used in the game.
    :param input_dict: the dictionary to be used.
    :type input_str: string
    :type input_dict: list
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


if __name__ == '__main__':
    main()