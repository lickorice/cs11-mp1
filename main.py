"""
    This is the .py file for starting the game
    Run this to run the game.
"""

import engine, interface, json

with open('config/cfg_general.json') as ofile:
    cfg_general = json.load(ofile)


def main():
    """The main method that is run when running the game."""
    engine.init_dictionary(cfg_general["DICTIONARY_FILE"])
    interface.start_game()


if __name__ == '__main__':
    main()