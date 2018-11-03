"""
    This is the main .py file. 
    Run this to run the game.

    developed by Carlos Panganiban, 2018
    github.com/lickorice | @cgpanganiban
"""

import engine, interface, json

with open('config/cfg_general.json') as ofile:
    cfg_general = json.load(ofile)


def main():
    """The main method run when running the game."""
    engine.init_dictionary(cfg_general["DICTIONARY_FILE"])
    interface.start_game()


if __name__ == '__main__':
    main()