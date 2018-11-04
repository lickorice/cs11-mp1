"""
    This module is only run when **Pygame is not installed in the system.**
"""


print("Running CLI fallback version...")

import engine, json, sys, time, os

this_directory = os.path.dirname(__file__)
with open(os.path.join(this_directory, 'config/cfg_cli.json')) as ofile:
    int_str = json.load(ofile)


def input_prompt(mistakes):
    """
    This is the equivalent of the mistake counter
    in the original Pygame rendition. However,
    this is integrated to the input prompt in the CLI.

    :returns: (`bool`) if the time has ended or if mistakes reach 3, (`string`) the prompt string.

    :param mistakes: the number of mistakes the player currently has.

    :type mistakes: int
    """

    if mistakes >= 3:
        return True, ''

    prompt_str = "( {0[0]} {0[1]} {0[2]} ) Enter your answer: "
    mistakes_list = []
    for i in range(mistakes):
        mistakes_list.append('X')
    for i in range(3-mistakes):
        mistakes_list.append('_')

    prompt_str = prompt_str.format(mistakes_list)
    return False, prompt_str


def anagram_screen():
    """This function instantiates the anagram screen."""
    # Loading screen:
    display_word, answer_list = engine.anagram_init()

    print("======================")
    print("     ANAGRAM MODE     ")
    print("======================")

    while len(answer_list) < 3:
        print("Choosing a word: " + display_word, end=' '*20 + '\r', flush=True)
        display_word, answer_list = engine.anagram_init()
    print("A word has been chosen!" + ' '*20)
    print("The word is: " + display_word)

    original_list = answer_list.copy()

    mistakes, game_ended = 0, False

    while True:
        
        game_ended, prompt_string = input_prompt(mistakes)

        if game_ended or len(answer_list) == 0:
            print("Game over!")
            break

        answer = input(prompt_string)
        if answer.lower() in answer_list:
            print("Correct answer!")
            answer_list.remove(answer.lower())
            engine.anagram_correct()
        else:
            print("Sorry, try again!")
            mistakes += 1

    words_solved = engine.anagram_end()
    plurality = 's' if words_solved != 1 else ''

    print("Nice work! You solved {} word{}!".format(words_solved, plurality))
    print("The anagrams for {} are:".format(display_word))
    printer = [print(x) for x in original_list]
    print("\n===================================")
    print("Redirecting you to the main menu...")
    print("===================================")
    start_menu()


def combine_screen():
    """This function instantiates the anagram screen."""

    print("======================")
    print("     COMBINE MODE     ")
    print("======================")
    print(" INITIALIZING POOL... ")
    print("======================")

    letter_string, max_points = engine.combine_init()

    print("======================")
    print("|  LETTER POOL  |")
    print("+---------------+")
    ltr_row = '|'
    for i in range(0, 8):
        ltr_row += '{}|'.format(letter_string[i].upper())
    print(ltr_row.rstrip())
    print("+-+-+-+-+-+-+-+-+")
    ltr_row = '|'
    for i in range(8, 16):
        ltr_row += '{}|'.format(letter_string[i].upper())
    print(ltr_row.rstrip())
    print("+---------------+")

    mistakes, answer_list = 0, []

    while True:
        
        game_ended, prompt_string = input_prompt(mistakes)
        current_points = engine.combine_points()

        if game_ended or current_points >= max_points:
            print("Game over!")
            break

        answer = input(prompt_string)

        if answer.lower() in answer_list:
            print("Sorry, try again!")
            mistakes += 1
            continue

        if engine.combine_correct(answer.lower(), letter_string):
            print("Correct answer!")
            answer_list.append(answer.lower())
        else:
            print("Sorry, try again!")
            mistakes += 1

    points = engine.combine_end()
    plurality = 's' if points != 1 else ''

    print("Nice work! You solved {} word{}!".format(points, plurality))
    print("The max points for {} is {} points!.".format(letter_string, max_points))
    print("\n===================================")
    print("Redirecting you to the main menu...")
    print("===================================")
    start_menu()


def start_menu():
    """This function shows the main menu in CLI mode."""
    print(int_str["MAIN_MENU"])
    while True:
        user_input = input(int_str["MENU_PROMPT"])
        if user_input in "123" and user_input != '':
            break
    if user_input == "1":
        anagram_screen()
    elif user_input == "2":
        combine_screen()
    elif user_input == "3":
        print(int_str["EXIT_MSG"])
        quit()


def start_game():
    """This function starts the game in CLI mode."""
    start_menu()