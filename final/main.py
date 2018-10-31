"""
    This is the main .py file. 
    Run this to run the game.

    developed by Carlos Panganiban, 2018
    github.com/lickorice | @cgpanganiban
"""

import engine, interface, json, sys, player

with open ("assets/cli_strings.json") as ofile:
    cli_strings = json.load(ofile)


def main():
    """
    The main method run when running the game.
    """

    print("Initializing game...")

    # Initiate the main dictionary
    _dict = engine.init_dictionary()
    if _dict[0]:
        print("Dictionary successfully loaded. {} words found.".format(_dict[1]))
    else:
        print("Dictionary failed to load. Exiting game...")
        return

    print("Initializing anagram library...")

    _dict2 = engine.init_anagram_dict(3)
    if _dict2[0]:
        print("Anagram library successfully loaded. {} words found.".format(_dict2[1]))
    else:
        print("Anagram library failed to load. Exiting game...")
        return
    
    print(cli_strings["MAIN-MENU"])

    while True:
        try:
            usr_input = int(input("Enter selection (1-3): "))
        except ValueError:
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            continue
        if usr_input == 1:
            if not game_mode_select():
                continue
            else:
                print(cli_strings["MAIN-MENU"])
                continue
        elif usr_input == 2:
            pass # TODO: highscores page
        elif usr_input == 3:
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            print("Thanks for playing!\nExiting game...")
            return
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")


def game_mode_select():
    print(cli_strings["GAME-SELECTION"])
    _player = player.Player()
    while True:
        try:
            usr_input = int(input("Enter selection (1-3): "))
        except ValueError:
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            continue
        if usr_input == 1:
            engine.start_game(1, _player)
            return True
        elif usr_input == 2:
            engine.start_game(2, _player)
            return True
        elif usr_input == 3:
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            print("Going back...")
            print(cli_strings["MAIN-MENU"])
            return False
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")



if __name__ == '__main__':
    main()